var gulp = require('gulp');
var jshint = require('gulp-jshint');
var bower = require('gulp-bower');
var bowerFiles = require('main-bower-files');
var inject = require('gulp-inject');
var connect = require('gulp-connect');
var inject = require('gulp-inject');

gulp.task('bower', function() {
  return bower();
});

gulp.task('lint', function() {
	return gulp.src('./app/js/*.js')
		.pipe(jshint())
		.pipe(jshint.reporter('default'));
});

gulp.task('inject', function () {

    return gulp.src('./app/index.html')
        .pipe(inject(
            gulp.src(['./app/js/*.js', './app/css/*.css'], {read: false}, {relative: true})
        ))
        .pipe(gulp.dest('./app'));
});

gulp.task('connect', function() {
    connect.server({
        root: 'app',
        livereload: true
    });
});

gulp.task('bower-files', function(){
    return gulp.src(bowerFiles({
    		'overrides': {
    			'bootstrap': {
    				'main': [
    					'./dist/css/bootstrap.min.css'
    				]
    			},
    		}
    	}))
    	.pipe(gulp.dest('./app/lib'));
});

gulp.task('build', ['lint', 'bower-files', 'inject'], function() {
	return gulp.src('./app/**')
		.pipe(gulp.dest('./build'));
});

gulp.task('watch', function() {
	gulp.watch('app/js/**/*.js', ['lint']);
});

gulp.task('default', ['bower', 'watch', 'inject']);