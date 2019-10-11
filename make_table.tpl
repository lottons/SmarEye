<head>
<style type="text/css">
table, th , td  {
  border: 1px solid grey;
  border-collapse: collapse;
  padding: 5px;
}
table tr:nth-child(odd) {
  background-color: #f1f1f1;
}
table tr:nth-child(even) {
  background-color: #ffffff;
}
</style>
</head>
<body>
<font size="3">当前剩余车位：</font>
<font size="5" color="#FF0000">{{count}}</font>
<p></p>
<table border="1">
<tr>
<td>车位编号</td>
<td>状态</td>
</tr>
<tr>
  <td>01</td>
  <td><img src="./images/{{rows[0]}}.png" alt="Smiley face" width="20" height="20"></td>
</tr>
<tr>
  <td>02</td>
  <td><img src="./images/{{rows[1]}}.png" alt="Smiley face" width="20" height="20"></td>
</tr>
<tr>
  <td>03</td>
  <td><img src="./images/{{rows[2]}}.png" alt="Smiley face" width="20" height="20"></td>
</tr>
<tr>
  <td>04</td>
  <td><img src="./images/{{rows[3]}}.png" alt="Smiley face" width="20" height="20"></td>
</tr>
</table>
<p>图示：</p>
<table>
<tr>
<td>空闲</td>
<td><img src="./images/green.png" alt="Smiley face" width="20" height="20"></td>
</tr>
<tr>
<td>占用</td>
<td><img src="./images/red.png" alt="Smiley face" width="20" height="20"></td>
</tr>
</table>
</body>
