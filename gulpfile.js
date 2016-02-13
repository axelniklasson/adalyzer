var gulp = require('gulp');
var jshint = require('gulp-jshint');
var bower = require('gulp-bower');
var bowerFiles = require('main-bower-files');

gulp.task('bower', function() {
  return bower();
});

gulp.task('lint', function() {
	return gulp.src('./app/js/*.js')
		.pipe(jshint())
		.pipe(jshint.reporter('default'));
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

gulp.task('build', ['lint', 'bower-files'], function() {
	return gulp.src('./app/**')
		.pipe(gulp.dest('./build'));
});

gulp.task('watch', function() {
	gulp.watch('app/js/**/*.js', ['lint']);
});

gulp.task('default', ['bower', 'watch']);