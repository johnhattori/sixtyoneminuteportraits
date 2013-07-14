module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    coffee: {
      compile: {
        files: { 'public/main.js': 'src/main.coffee' }
      }
    },
    copy: {
      main: {
        files: [{expand: false, src: 'src/index.html', dest: 'public/index.html'}]
      }
    },
    sass: {
      dist: {
        files: {
          'public/style.css': 'src/style.scss'
        }
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-coffee');
  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-copy');

  // Default task(s).
  grunt.registerTask('default', ['coffee','copy', 'sass']);

};