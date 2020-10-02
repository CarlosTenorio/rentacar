from typing import List
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
import json

######################
# FIRST VERSION VIEWS
######################


def _create_mock_cars(toJson: bool = False):
    class Car():
        def __init__(self,
                     id: int,
                     doors: int,
                     wheels: int,
                     brand: str,
                     model: str,
                     registrationId: str):
            self.id = id
            self.doors = doors
            self.wheels = wheels
            self.brand = brand
            self.model = model
            self.registrationId = registrationId

        def toJson(self):
            return json.dumps(self, default=lambda o: o.__dict__)

        def __str__(self):
            return f"Id: {self.id}, brand: {self.brand}, model: {self.model}, registration: {self.registrationId}"

    car1 = Car(0, 3, 4, 'Porshe', '911', None)
    car2 = Car(1, 5, 4, 'Hyundai', 'i30', '345PJK')
    if (toJson):
        return [car1.toJson(), car2.toJson()]
    else:
        return [car1, car2]


def findCar(car_id: int, cars: List):
    for car in cars:
        # print('Loop: ' + str(car.id))
        if car.id == car_id:
            return car
    return None

# Create your views here.


class CarViewSet(viewsets.ViewSet):
    """
    GET (ALL)
    """

    def list(self, request, format=None):
        return Response({'cars': _create_mock_cars(True)}, status=status.HTTP_200_OK)
    """
    GET (ONE)
    """

    def retrieve(self, request, id=None):
        print(id)
        cars = _create_mock_cars()
        # Same behaviour, differents options.
        # car_to_return = next((car for car in cars if car.id == id), None)
        car_to_return = findCar(id, cars)
        if(car_to_return):
            return Response({'cars': car_to_return.toJson()}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    """
    POST
    """

    def create(self, request):
        cars = _create_mock_cars()
        new_car = request.data
        # print(new_car)
        new_car['id'] = len(cars)
        cars.append(new_car)
        print(cars[1])
        return Response(new_car, status=status.HTTP_201_CREATED)
    """
    PUT
    """

    def update(self, request, id=None):
        cars = _create_mock_cars()
        car_to_return = findCar(id, cars)
        if(car_to_return):
            car_updated = request.data

            # DIRTY VERSION
            # if('doors' in car_updated):
            #     car_to_return.doors = car_updated['doors']
            # if('wheels' in car_updated):
            #     car_to_return.wheels =car_updated['wheels']
            # if('brand' in car_updated):
            #     car_to_return.brand = car_updated['brand']
            # if('model' in car_updated):
            #     car_to_return.model = car_updated['model']
            # if('registrationId' in car_updated):
            #     car_to_return.registrationId = car_updated['registrationId']

            # CLEAN VERSION
            for key in car_updated:
                if(getattr(car_to_return, key)):
                    setattr(car_to_return, key, car_updated[key])

            return Response({'cars': car_to_return.toJson()}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    """
    DELETE
    """

    def destroy(self, request, id=None):
        cars = _create_mock_cars()
        for car in cars:
            if car.id == id:
                cars.remove(car)
                print("I found it!")
                break
        else:
            raise HTTPException(status_code=404, detail="Item not found")
        return cars

    def get_queryset(self):
        return

#########################################
# SECOND VERSION VIEWS (DB integration)
########################################
