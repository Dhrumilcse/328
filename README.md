# 328
A platform to let you buy and sell nfts, built with Django, PostgreSQL, and Heroku.

<add an image>

## Features

Talk about the features and yet to implement features

<add a gif buy page>

## Run locally

Instructions to run locally goes here

## Test Cases
Working with images requires successful generation and deletion of the same. Using a helper function to create a temporary test_image and using that to test whether our model can upload a new image or not. Payments, Account, and Nft (main app): each application contains test cases in their respective tests.py files.

``` 
# shop/nft/tests.py

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

Discuss some test cases and why they are important

## Upcoming Features
 - [ ] Delete Image
 - [ ] Sort by New, Old, and Title
 - [ ] Upload Bulk Images
