<?php
echo'<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script type="text/javascript">
        function validate() 
        {
            var user = document.getElementsByName("username");
            var fname=document.getElementsByName("fname");
            var lname=document.getElementsByName("lname");
            var gender=document.getElementsByName("gender");
            var pass=document.getElementsByName("pass")
            if (user[0].value == "") {
                alert("Enter a username");
            }
            if (fname[0].value == "") {
                alert("Enter a firstname");
            }
            if (lname[0].value == "") {
                alert("Enter a lastname");
            }
            if (gender.length<0 && gender[0].value == "") {
                alert("Enter a gender");
            }
            if (pass[0].value == "") {
                alert("Enter a password");
            }
        }
    </script>    
</head>
<body>
    <h1 style="text-align: center;">Student Registration</h1>
    <table align="center" style="border-collapse: collapse;">
        <tr>
            <td>username:</td>
            <td><input type="text" name="username"></td>
        </tr>
        <tr>
            <td>fname:</td>
            <td><input type="text" name="fname"></td>
        </tr>
        <tr>
            <td>lname:</td>
            <td><input type="text" name="lname"></td>
        </tr>
        <tr>
            <td>Gender:</td>
            <td>Male<input type="radio" value="male" name="gender">Female<input type="radio" value="male" name="gender"></td>
        </tr>
        <tr>
            <td>password:</td>
            <td><input type="password" name="pass"></td>
        </tr>
        <tr>
            <td colspan="2"><input style="width: 100%;" type="submit" name="submit" onclick="validate()"></td>
        </tr>
    </table>
</body>
</html>';
?>