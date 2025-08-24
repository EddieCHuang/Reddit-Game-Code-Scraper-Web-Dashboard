<a id="readme-top"></a>


[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">


<h3 align="center">Reddit Game Code Scraper</h3>

  <p align="center">
    A reddit game code scarper that get reward code.
    <br />
    <a href="https://github.com/EddieCHuang/Reddit-Game-Code-Scraper-Web-Dashboard"><strong>Explore the docs »</strong></a>
    <br />
    <br />

  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
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
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
A reddit game code scraper with a simple web dashboard.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![FLASK][Flask.py]][Flask-url]
* [![PRAW][Praw.py]][Praw-url]
* [![jsdelivr][Jsdelivr.html]][Jsdelivr-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.


### Installation

1. Get a free API Key at [https://www.reddit.com/dev/api/](https://www.reddit.com/dev/api/)
2. Clone the repo
   ```sh
   git clone https://github.com/EddieCHuang/Reddit-Game-Code-Scraper-Web-Dashboard.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `scraper.py`
   ```
    reddit = praw.Reddit(enter your api key)
   ```
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin EddieCHuang/Reddit-Game-Code-Scraper-Web-Dashboard
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Eddie Huang - supereddieh@gmail.com

Project Link: [https://github.com/EddieCHuang/Reddit-Game-Code-Scraper-Web-Dashboard](https://github.com/EddieCHuang/Reddit-Game-Code-Scraper-Web-Dashboard)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/eddie-huang27/
[Flask.py]: https://img.shields.io/badge/Flask-Framework-lightgrey?logo=flask
[Flask-url]: https://flask.palletsprojects.com/en/stable/
[Praw.py]: https://img.shields.io/badge/PRAW-Reddit_API_Wrapper-ff4500?logo=reddit&logoColor=white
[Praw-url]: https://praw.readthedocs.io/en/stable/
[Jsdelivr.html]: https://img.shields.io/jsdelivr/npm/hm/axios
[Jsdelivr-url]: https://www.jsdelivr.com/
