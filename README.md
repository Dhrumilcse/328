# 328
A minimal platform to let you buy and sell nfts, built with Django, PostgreSQL, and Heroku.

<img src="https://github.com/Dhrumilcse/328/blob/main/readme_media/home.png"> <br>

## Features
1. Upload/buy page won't let you in if you are not an authenticated user (access control)
2. Using AWS S3 for securely storing and retrieving user uploaded images directly, and using [WhiteNoise](http://whitenoise.evans.io/en/stable/) to serve static files since it serves compressed content and compression can make dramatic reductions in the bandwidth required for your CSS and JS.
3. A recommendation of other similar images (selecting random at the moment, a simple recommendation based on tags is WIP)
4. Search for an image (based on title and/or tags)
5. Payment was handled using secure Stripe Checkout API. <br><br>
<img src="https://github.com/Dhrumilcse/328/blob/main/readme_media/payment.png"> <br>

<add a gif buy page>

## Run locally

Instructions to run locally goes here

## Test Cases
Working with images requires successful generation and deletion of the same. Using a helper function to create a temporary test_image to test whether or not our model can upload a new image. Payments, Account, and Nft (main app): each application contains test cases in their respective tests.py files.

``` 
# 328/nft/tests.py

# Image upload test
class ImageUploadTest(TestCase):

    # Changing media_root to a temp dir to prevent filiing our media dir with garbage
    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_image_upload(self):
        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temporary_image(temp_file)
        image = Nft.objects.create(image=test_image.name)
        self.assertEqual(len(Nft.objects.all()), 1)
  ```


## Upcoming Features
 - [ ] Containerize application using Docker for easier local tests
 - [ ] Delete Image
 - [ ] Sort by New, Old, and Title
 - [ ] Upload Bulk Images
