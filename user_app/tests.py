
from django.test import Client
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from django.urls import reverse
from .views import *
from .models import *
import json
# Create your tests here.
client = Client()

class GetParentTest(APITestCase):
    """
    Test module for getting list of parents or get a single parent instance
    """
    def setUp(self):
        test_address1 = {
            "street": "Cyberjaya",
            "city": "Gurgaon",
            "state": "Haryana",
            "zip": 69
            }
        
        test_address2 = {
            "street": "06",
            "city": "Dhaka",
            "state": "Dhaka",
            "zip": 880
        }
        
   
        test_child1 = {
                "first_name": "Ahnaf",
                "last_name": "Atef",
                }
        
        test_parent1 = {
            "first_name": "Sohaib",
            "last_name": "Siddiquee",
            }
        test_parent2 = {
            "first_name": "Nibras",
            "last_name": "Kabir",
            }
        

        
        address1 = Address.objects.create(**test_address1)
        self.parent1 = Parent.objects.create(**test_parent1,address=address1)
        self.child1 = Child.objects.create(**test_child1,parent=self.parent1)  
        
        address2 = Address.objects.create(**test_address2)
        self.parent2 = Parent.objects.create(**test_parent2,address=address2)
       
        
        self.test_data = [
                {
                "id": 1,
                "first_name": "Sohaib",
                "last_name": "Siddiquee",
                "address": {
                "id": 1,
                "street": "Cyberjaya",
                "city": "Gurgaon",
                "state": "Haryana",
                "zip": 69
                },
                "children": [
                {
                    "id": 1,
                    "first_name": "Ahnaf",
                    "last_name": "Atef",
                    "parent": 1
                }
                ]
            },
            {
                "id": 2,
                "first_name": "Nibras",
                "last_name": "Kabir",
                "address": {
                    "id": 2,
                    "street": "06",
                    "city": "Dhaka",
                    "state": "Dhaka",
                    "zip": 880
                },
                "children": []
            }             
        ]
                 
    def test_get_all_parent(self):
        
        response = self.client.get(
            reverse('parent')
        )
          
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(json.loads(response.content),self.test_data)
        
        
    def test_get_one_parent(self):
  
        response = self.client.get(
            reverse('parent_detail',args=[self.parent1.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content,json.dumps(self.test_data[0]))
        

class CreateParentTest(APITestCase):
    
    """
    Test module for inserting a new parent
    """   
    
    def setUp(self):
        
        self.valid_payload = {
            "first_name": "Ahsan Sadman",
            "last_name": "Khan",
            "address": {
                "street": "Kalabagan",
                "city": "Dhaka",
                "state": "Dhaka",
                "zip": 880
                },
            "children" : []
        }
        self.invalid_payload = {
            "first_name": "Ahsan Sadman",
            "last_name": "",
            "address": {
                "id": 1,
                "street": "Kalabagan",
                "city": "Dhaka",
                "state": "Dhaka",
                "zip": 880
                }
        }
        self.test_data = {
            "id" : 1,
            "first_name": "Ahsan Sadman",
            "last_name": "Khan",
            "address": {
                "id" : 1,
                "street": "Kalabagan",
                "city": "Dhaka",
                "state": "Dhaka",
                "zip": 880
                },
            "children" : []
        }
        
    def test_valid_post_parent(self):
         
        response = self.client.post(
            reverse('parent'),
            json.dumps(self.valid_payload),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertJSONEqual(response.content,json.dumps(self.test_data))
    
    def test_invalid_post_parent(self):
        
        response = self.client.post(
            reverse('parent'),
            json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CreateChildTest(APITestCase):   
    """
    Test module for inserting a new child
    """   
    def setUp(self):
        
        test_address1 = {
            "street": "Cyberjaya",
            "city": "Gurgaon",
            "state": "Haryana",
            "zip": 69
            }
        test_parent1 = {
            "first_name": "Sohaib",
            "last_name": "Siddiquee",
            }
        
        self.parent = Parent.objects.create(**test_parent1,address=Address.objects.create(**test_address1))
        
        self.valid_payload = {
            "first_name": "Ahsan",
            "last_name": "Sadman",
            "parent": 1
            }
        self.invalid_payload = {
            "first_name": "Ahsan",
            "last_name": ""
            }
        
        self.test_data = {
            "id": 1,
            "first_name": "Ahsan",
            "last_name": "Sadman",
            "parent": 1
            }
        
    def test_valid_post_child(self):
        
        
        response = self.client.post(
            reverse('children'),
            json.dumps(self.valid_payload),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertJSONEqual(response.content,json.dumps(self.test_data))
    
    def test_invalid_post_child(self):
        
        response = self.client.post(
            reverse('children'),
            json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        

        
        
class UpdateDeleteParentTest(APITestCase):
    """ Test module for updating or deleting an existing parent record """

    def setUp(self):
        
        test_address1 = {
            "street": "Cyberjaya",
            "city": "Gurgaon",
            "state": "Haryana",
            "zip": 69
            }
   
        test_parent1 = {
            "first_name": "Sohaib",
            "last_name": "Siddiquee",
            }

        address1 = Address.objects.create(**test_address1)
        self.parent1 = Parent.objects.create(**test_parent1,address=address1)

        self.valid_payload = {
                "id": 1,
                "first_name": "Sohaib",
                "last_name": "Siddique",
                "address": {
                "id": 1,
                "street": "Gurugram",
                "city": "Gurgaon",
                "state": "Haryana",
                "zip": 69
                },
                "children": []
            }        
           
        self.invalid_payload = {
                "last_name": "Siddique",
                "address": {
                "id": 1,
                "street": "Gurugram",
                "city": "Gurgaon",
                "state": "Haryana",
                "zip": 69
                },
                "children": []
            }           
        
               
    def test_valid_put_parent(self):
        
        response = self.client.put(
            reverse('parent_detail', args=[self.parent1.id]),
            json.dumps(self.valid_payload),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertJSONEqual(response.content,json.dumps(self.valid_payload))
        
    def test_invalid_put_parent(self):
        
        response = self.client.put(
            reverse('parent_detail', args=[self.parent1.id]),
            json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_valid_delete_parent(self):
        
        response = self.client.delete(
            reverse('parent_detail', args=[self.parent1.id])
        )
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_invalid_delete_parent(self):
        
        response = self.client.delete(
            reverse('parent_detail', args=[30])
        )
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        
        
class UpdateDeleteChildTest(APITestCase):
    """ Test module for updating or deleting an existing child record """
    def setUp(self):
        
        test_address1 = {
            "street": "Cyberjaya",
            "city": "Gurgaon",
            "state": "Haryana",
            "zip": 69
            }
        test_parent1 = {
            "first_name": "Sohaib",
            "last_name": "Siddiquee",
            }
        test_child1 = {
                "first_name": "Ahnaf",
                "last_name": "Atef",
            }
        self.parent = Parent.objects.create(**test_parent1,address=Address.objects.create(**test_address1))
        self.child = Child.objects.create(**test_child1,parent=self.parent)
        
        self.valid_payload = {
            "first_name": "Ahsan",
            "last_name": "Sadman",
            "parent": 1
            }
        self.invalid_payload = {
            "first_name": "Ahsan",
            "last_name": ""
            }
        
        self.test_data = {
            "id": 1,
            "first_name": "Ahsan",
            "last_name": "Sadman",
            "parent": 1
            }
        
    def test_valid_put_child(self):
        
        
        response = self.client.put(
            reverse('child_detail',args=[self.child.id]),
            json.dumps(self.valid_payload),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertJSONEqual(response.content,json.dumps(self.test_data))
    
    def test_invalid_put_child(self):
        
        response = self.client.put(
            reverse('child_detail',args=[self.child.id]),
            json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_valid_delete_child(self):
        
        response = self.client.delete(
            reverse('child_detail', args=[self.child.id])
        )
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_invalid_delete_child(self):
        
        response = self.client.delete(
            reverse('child_detail', args=[30])
        )
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
