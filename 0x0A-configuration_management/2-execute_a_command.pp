#this is for my last task
exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow',
}
