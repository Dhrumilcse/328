# 328
A minimal platform to let you buy and sell nfts, built with Django, PostgreSQL, and Heroku. Submission for Shopify Data Developer Challenge Fall 2021.

https://user-images.githubusercontent.com/17984133/116902775-8b7f7000-ac09-11eb-87ca-5800b4f42867.mp4


## Features
1. Authentication and authorization using Django's inbuilt system which uses [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) algorithm with a SHA256 hash to store passwords. In addition, extended authentication support for third-party, in this case Github, using OAuth 2.0
1. [Buy](https://nft328.herokuapp.com/buy/2), [Profile](https://nft328.herokuapp.com/profile), [Upload](https://nft328.herokuapp.com/profile), and [Delete](https://nft328.herokuapp.com/3/delete) pages won't let you in if you are not an authenticated user (access control)
2. Using AWS S3 for directly and securely storing and retrieving user uploaded images (using [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)), and using [WhiteNoise](http://whitenoise.evans.io/en/stable/) to serve static files since it serves compressed content and compression can make dramatic reductions in the bandwidth required for your CSS and JS.
3. A recommendation of other similar images (selecting random at the moment, a simple recommendation based on tags is WIP)
4. Search for an image (based on title and/or tags)
5. Payment was handled using secure Stripe Checkout API. <br><br>
<img src="https://github.com/Dhrumilcse/328/blob/main/readme_media/payment.png"> <br>

## Test Cases
Working with images requires successful generation and deletion of the same, and that requires an authenticated user. Using a helper function to create a temporary test_image, setting up test user, and logging them in to test whether or not our model can upload a new image. Payments, Account, and Nft (main app): each application contains test cases in their respective tests.py files.

``` 
# 328/nft/tests.py

# Image upload test
class ImageUploadTest(TestCase):

    # Set-up test user since image uploads require authenticated user
    def setUp(self):
        self.user = User.objects.create_user(
            username='dhrumil',
            email='test@email.com',
            password='iloveshopify'
        )
        
        self.assertTrue(self.client.login(username='dhrumil', password='iloveshopify'))

    # Changing media_root to a temp dir to prevent filiing our media dir with garbage
    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_image_upload(self):
        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temporary_image(temp_file)
        image = Nft.objects.create(image=test_image.name)
        self.assertEqual(len(Nft.objects.all()), 1)
  ```

## Run locally

Working on containerizing the application for easier local runs. Until then, please follow instructions.
1. Clone the repository
```
git clone https://github.com/Dhrumilcse/328.git
```
2. Rename to maintin local settings
```
mv 328 shop
```

```
+-- 328_local
|   +-- shop
```

3. Create and activate virtual environment
```
# Create
virtualenv venv --python=python3

# Activate
source venv/bin/activate (for mac)
venv\Scripts\activate (for win)
```

```
+-- 328_local
|   +-- shop
|   +-- venv
```

4. Install dependencies
```
cd shop
pip install -r requirements.txt
```

5. Migrate database
```
python manage.py makemigrations
python manage.py migrate
```

6. Run server
```
python manage.py runserver
```

Visit [127.0.0.1:8000/](http://127.0.0.1:8000/) and you will see the app running.

## Upcoming Features
 - [ ] Containerize application using Docker for easier local tests
 - [x] Delete Image
 - [ ] Sort by New, Old, and Title
 - [ ] Upload Bulk Images
