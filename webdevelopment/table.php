<?php
$array=array(array('Ms dhoni',40),array('virat kholi',33),array('sachin tendulkar',48));
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <table border="1px solid black" align="center" style="border-collapse:collapse; height:400px;width:400px;">
        <tr>
            <th>Name</th>
            <th>Age</th></tr>
        <tr>
            <td><?php echo $array[0][0] ?></td>
            <td><?php echo $array[0][1] ?></td>
        </tr>
        <tr>
            <td><?php echo $array[1][0] ?></td>
            <td><?php echo $array[1][1] ?></td>
        </tr>
        <tr>
            <td><?php echo $array[2][0] ?></td>
            <td><?php echo $array[2][1] ?></td>
        </tr>
    </table>
</body>
</html>