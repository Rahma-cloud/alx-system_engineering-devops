# Puppet Manifest for Nginx configuration

class nginx {
  # Install Nginx package
  package { 'nginx':
    ensure => installed,
  }

  # Ensure the Nginx service is running
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }

  # Copy the Nginx configuration file
  file { '/etc/nginx/nginx.conf':
    ensure  => present,
    source  => 'puppet:///modules/nginx/nginx.conf',
    require => Package['nginx'],
    notify  => Service['nginx'],
  }
}

# Apply the nginx class
include nginx

