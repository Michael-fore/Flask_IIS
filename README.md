# Flask_IIS

Reposity for a youtube tutorial on how to run a flask app in IIS.

0. Clone this repo to wwwroot

1. Install Python in the root directory

2. Enable CGI for IIS

3. Install wfastcgi from pip

4. Ensure proper file permissions 

5. Configure Web.config

Youtube Tutorial: https://youtu.be/En9vo7Ognm0


# Contact

[Add me on Linkedin](https://www.linkedin.com/in/michael-fore-11a46a58/), if you want any custom work done this is a good place to reach me.

I don't use [Twitter](https://twitter.com/Wolfman_Brother) all that much, but here it is.

# FAQ/Troubleshooting:

1. HTTP Error 500.0 - Internal Server Error<handler> scriptProcessor could not be found in <fastCGI> application configuration
a. Make sure the path in your FastCGI settings in IIS home matches what is inside the web.config
  Here is an example of what can cause this error.
  ![image](https://user-images.githubusercontent.com/4061343/126227544-c79ad1ac-0cca-4c27-9cd5-2d886e6ada96.png)
