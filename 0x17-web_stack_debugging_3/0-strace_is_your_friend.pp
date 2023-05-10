## A puppet script for error correction in a web server

$php_file_path = '/var/www/html/wp-settings.php'

exec { 'replace_php_line':
command => "sed -i 's/phpp/php/g' ${php_file_path}",
path => ['/bin','/usr/bin']
}
