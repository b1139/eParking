# eParking
eParking System API - Python + Django
API Manages the parking system

# This is a simple API for:

* Parking your vehicle
* UnParking your vehicle
* API Throttling, defends the API Usages limit

# Table of Contents

* [Requirements](#requirements) 
* [Installation](#installation)
* [Test](#test)
* [RunServer](#runserver)
* [API](#api)
* [Throttling](#throttling)

# Requirements

* Python 3.7 <

# Installation

Install using `pip`...

    pip install -r requirements.txt

Create application related models
    
    python manage.py migrate
   
# Test

Please look in eParking/api/test.py for list of test cases implemented

Test the core functionality of the eParking System using below command

    python manage.py test
    will output
        ----------------------------------------------------------------------
        Ran 4 tests in 40.320s
        OK
        
# RunServer

run using below command `manage.py`

    python manage.py runserver


# API

**Prefix:** /api/v1

**/park**

* post 
    Parks a Car/Bike and returns the slot no where it is parked
    
    URL: http://servername:port/api/v1/park/
    
    data = {"vehicle.registration_no": "SG 1234 23"}
    
    response = {"slot_no": 1}

**/park/<slot_no>**

* delete
    Un Parks your vehicle by the given slot number and frees that particular slot for use
    
    URL: http://servername:port/api/v1/park/1/
    
    response = {"message": "Slot 1 is available for parking now"}
 
 **/park_info/**
 Lists the list of slots and parked vechile information
  
  * get
  
    List all
    
        * URL: http://servername:port/api/v1/park_info/
        
            response => [
                    {
                        "slot_no": 1,
                        "parked_vehicle": "SG 380939"
                    },
                    {
                        "slot_no": 2,
                        "parked_vehicle": "SG WE 9900"
                    },
                    {
                        "slot_no": 3,
                        "parked_vehicle": "SW 2299 0011"
                    }
                ]
                
    Filter By Slot
    
        * URL: http://servername:port/api/v1/park_info/?slot_no=1
        
            response => [
                            {
                                "slot_no": 1,
                                "parked_vehicle": "SG 380939"
                            }
                        ]
                        
    Filter By Vehicle Registration No
    
        * URL: http://servername:port/api/v1/park_info/?parked_vehicle__registration_no=SW 2299 0011
        
            response => [
                            {
                                "slot_no": 3,
                                "parked_vehicle": "SW 2299 0011"
                            }
                        ]


# Throttling

The server will rate-limit the number of requests coming in. 

If an user makes more than 10 requests in 10 seconds to the above APIs, You will get to see the below message
    
    {"detail":"Request was throttled. Expected available in 5 seconds."}