# Adalyzer
Team "Murphy's lag"'s contribution to the Ericsson Automotive Hackaton 2016.

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
### Johan Angsúes

### Joakim Berntsson

### Tim Kerschbaumer

### Axel Niklasson
