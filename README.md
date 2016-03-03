# Adalyzer
Team Murphy's lag's contribution to the Ericsson Automotive Hackaton 2016.

## About
Adalyzer is a web application that analyses traffic flow in order to determine optimized advertising. By sampling data from the Interchange API and analyzing it the goal was to present three key points:

* Optimized advertising placement, depending on traffic flow
* Generated personas, calculated by [IBM Watson's Personality Insights API](http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/personality-insights.html) using tweets from appropriate sources as source
* Personas mapped to ad placements, providing an overview of what people might be interested in and where that content should be displayed 

## Implementation
The backend is written in Python which connects to the Interchange API and analyzes the data and serves it through [Flask](http://flask.pocoo.org/) to the frontend. The frontend is written in [AngularJS](https://angularjs.org/) using [Bootstrap](http://getbootstrap.com/) for the UI components. Everything is built with [Gulp.js](http://gulpjs.com/).

Since there were limited time to implement everything during the Hackathon and we ran into some severe problems with different backend development environments, the running application is using static data. However, the backend functionality is there - it is just not connected to the frontend.

## Build and run
### Build

For demo purposes, a working build is located at ```demo/```.

First make sure that you have [npm](https://www.npmjs.com/) installed globally on your computer.

To build Adalyzer, perform the following steps.
```
git clone https://github.com/axelniklasson/adalyzer.git
cd adalyzer
npm install
gulp build
```

### Run
We did not have time to implement automatic serving using Gulp, so just open ```build/index.html``` in your favourite web browser to run the app. Future development should use automatic serving, such as [gulp-serve](https://www.npmjs.com/package/gulp-serve).

## Team members
Below follow short presentations of the team members.
### Johan Angséus
My name is Johan Angséus and I'm currently enrolled to the Computer Systems and Networks master programme at Chalmers University of Technology. I'm fond of all kinds of developing, especially backends and systems.
[GitHub](https://github.com/angseus) and
[angseus.ninja](http://angseus.ninja) 

### Joakim Berntsson
My name is Joakim Berntsson and I am studying my third year of Software Engineering at Chalmers Univeristy of Technology. Besides my studies I have founded my own company, where I work with app and web development. When I am not working or studying I enjoy participating in events such as Hackathons to meet people and broaden my knowledge base. 

[GitHub](https://github.com/jcberntsson/), 
[LinkedIn](https://se.linkedin.com/in/joakimberntsson), 
[jcbit.se](http://jcbit.se)

### Tim Kerschbaumer
My name is Tim Kerschbaumer and I'm currently studying my third year at the Software Engineering programme at Chalmers. I recently started working at CTK (Chalmers Teknologkonsulter) and I enjoy participating in hackathons. I fancy all kinds of software development but I have recently started taking big interest in machine learning applications.

[GitHub](https://github.com/timkersch), 
[LinkedIn](https://www.linkedin.com/in/timkerschbaumer/), 
[timkersch.github.io](http://timkersch.github.io).


### Axel Niklasson
My name is Axel Niklasson and I am currently studying my third year of Software Engineering at Chalmers University of Technology. When I don't study or participate in hackathons, I work as a software consultant at my own firm, where I usually work with web development - both frontend and backend. However, I tend to focus more on backend since I find that more enjoyable at the moment. Below you can find the usual links and also my CV.

[GitHub](https://github.com/axelniklasson), 
[LinkedIn](https://se.linkedin.com/in/axel-niklasson-a1b43287), 
[axelniklasson.se](http://axelniklasson.se) and my
[CV](http://axelniklasson.se/media/CV_en.pdf).
