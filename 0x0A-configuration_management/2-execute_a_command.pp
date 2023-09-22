#this is for my last task
exec { 'kill_killmenow_process':
  command     => 'pkill killme now',
  refreshonly => true,
}
service { 'my_service':
  ensure  => 'running',
  require => Exec['killmenow'],
}
