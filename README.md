![](https://raw.githubusercontent.com/unton3ton/PyTorch-in-Flask/refs/heads/main/photo_2025-01-31_13-10-27.jpg)

```bash
FLASK_ENV=development FLASK_APP=app.py flask run
```
 
![](https://raw.githubusercontent.com/unton3ton/PyTorch-in-Flask/refs/heads/main/cat.jpg)
 
![](https://raw.githubusercontent.com/unton3ton/PyTorch-in-Flask/refs/heads/main/dog.jpg)
 
```bash
python requuuuest.py   
{'class_id': 'n02123394', 'class_name': 'Persian_cat'}  
{'class_id': 'n02099601', 'class_name': 'golden_retriever'}
```
 
![](https://raw.githubusercontent.com/unton3ton/PyTorch-in-Flask/refs/heads/main/lion.jpg)
 
```python
resp = requests.post("http://127.0.0.1:5000/predict",
                     files={"file": open('lion.jpg','rb')})
print(resp.json())
```
 
```bash
{'class_id': 'n02129165', 'class_name': 'lion'}
```
 
# Source
 
* [Deploying PyTorch in Python via a REST API with Flask](https://pytorch.org/tutorials/intermediate/flask_rest_api_tutorial.html)
 
[![ams2.jpg](https://i.postimg.cc/F15jMCyX/ams2.jpg)](https://postimg.cc/wR2yJV4w)
 
![](https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1y4v0B.img?w=612&h=437&m=6)

![](https://raw.githubusercontent.com/unton3ton/PyTorch-in-Flask/refs/heads/main/kMN1JmPeofY.jpg)
