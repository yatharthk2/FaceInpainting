<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
<!--[![Stargazers][stars-shield]][stars-url]-->
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
<!--[![LinkedIn][linkedin-shield]][linkedin-url]-->



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/yatharthk2/Inpainting">
    <img src="https://github.com/yatharthk2/Inpainting/blob/master/ivg/Inpainting_img.png" alt="Logo" width="1080" height="500">
  </a>

  <p align="center">
    <h3 align="center">An image reconstruction project using concepts of partial convolution</h3>
    <br />
    <a href="https://github.com/yatharthk2/Inpainting"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/yatharthk2/Inpainting/blob/master/result.jpg">View Demo</a>
    ·
    <a href="https://github.com/yatharthk2/Inpainting/issues">Report Bug</a>
    ·
    <a href="https://github.com/yatharthk2/Inpainting/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project



![](https://github.com/yatharthk2/Inpainting/blob/master/ivg/train%20video.gif)

This is a very unique project in itself as  very recently the concept of partial convolutions was introduced to the world [december 2018], before partial convolution we used to use algorithms such as PatchMatch, Iizuka et al, Yu et al and even the KNN for image reconstruction but there were two huge setbacks to these algorithms, which were :
1) Since the algorithms were ignorant of the different objects in the image, they often tended to smoothen the whole reconstruction, which was good to human eyes but lacked the actual information in terms of object segregation.
2) Another limitation of many recent approaches is the focus on rectangular-shaped holes, often assumed to be the center of the image. We find these limitations may lead to overfitting to the rectangular holes and ultimately limit the utility of these models in application

So to overcome the above 1st issue, a segmentation aware approach was used wherein the distorted image as well as the binary mask is inputted to the model as a result of which the model becomes aware of segmentations and different edges of the many objects in the image. Since the model is now aware of the segments it can more accurately segregate between the two objects.
To overcome the 2nd issue, various methods have been documented by the authors of the Pconv research paper, but the Random Walk algorithm was chosen to generate a random mask for the model to train upon so that it does not overfit a particular hole point.

Coming on to the aim of FaceInpainting, We saw that if we train the model on large datasets of images containing a single person then maybe we can teach the model to specifically reconstruct the distorted photo of a person. So to test the extent or limit to which we can reconstruct the broken image we trained the model with 50,000 images as training data, 5000 images as test data, and 5000 images as validation data for 1 million iterations.
To download the datasets and weights
<a href="https://drive.google.com/drive/folders/1E482OOOe_xYWVE9nKCnF_hrh0aLHgZIN?usp=sharing">click here</a>

### Architecture
<img src="https://github.com/yatharthk2/Inpainting/blob/master/ivg/architecture.jpg" alt="Logo" width="1080" height="300">

### Built With

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)
* [Laravel](https://laravel.com)



<!-- GETTING STARTED -->
## Getting Started

Step 1. Clone the repository.

Step 2. Download the dataset and pretrained weights from <a href="https://drive.google.com/drive/folders/1E482OOOe_xYWVE9nKCnF_hrh0aLHgZIN?usp=sharing">Here</a> and place it in the same directory.

### Installation

* Python 3.6+
* Install Pytorch

  (for cude 10.2 – GPU)
  ```sh
  pip install torch==1.9.0+cu102 torchvision==0.10.0+cu102 torchaudio===0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
  ```
  (for CPU)
  ```sh
  pip install torch torchvision torchaudio
  ```
  
* Install python libraries
  ```sh
  pip install -r requirements.txt
  ```

### Training

* Start from scratch
  ```sh
  python train.py
  ```
* Resume training
  ```sh
  python train.py --resume <weights_path>
  ```
### Testing

* Run the command line
  ```sh
  python run.py --photo <test_image_path>
  ```
* Draw Mask
* Press "s"

Output will be saved in the root directory in ```result.jpg``` format. 


<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/yatharthk2/Inpainting?color=red&label=contributors&logo=github&logoColor=green&style=for-the-badge
[contributors-url]: https://github.com/yatharthk2/Inpainting/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/yatharthk2/Inpainting?color=red&logo=github&logoColor=green&style=for-the-badge
[forks-url]: https://github.com/yatharthk2/Inpainting/network/members
<!--[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge-->
<!--[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers-->
[issues-shield]: https://img.shields.io/bitbucket/issues-raw/yatharthk2/Inpainting?color=red&logo=github&logoColor=green&style=for-the-badge
[issues-url]:https://github.com/yatharthk2/Inpainting/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/yatharthk2/Inpainting/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: C:\Users\yatha\OneDrive\Desktop\projects\Inpainting_project\Inpainting\train_video.gif
