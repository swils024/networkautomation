=================================
Linux Shell Script:
=================================
for x in 1 2 3
 do
 ping 10.1.1.$x
 done
 
function testping(){
 ping 10.1.1.1
  ping 10.1.1.2
  ping 10.1.1.3
  ping 10.1.1.4
}

 
function testecho(){
 echo 10.1.1.1
  echo 10.1.1.2
  echo 10.1.1.3
  echo 10.1.1.4
}

