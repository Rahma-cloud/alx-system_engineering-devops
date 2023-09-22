#this is for my last task
exec { 'kill_killmenow_process':
  command => 'pkill killme now',
  onlyif  => 'pgreo killmenow',
}
