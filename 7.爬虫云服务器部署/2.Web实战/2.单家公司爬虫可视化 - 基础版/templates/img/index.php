<!DOCTYPE HTML>
<html>
<head>
	<meta http-equiv="content-type" content="text/html charset=utf-8" />
	<meta name="author" content="Kimol" />
    <link rel="shortcut icon" type="image/x-icon" href="./img/logo.ico" />
	<title>华小智舆情监控系统</title>
    <style>.alsp{ font-family:"楷体"; font-size:100px}</style>
    <p align="center"><font size="5" color="#FFFFFF" face = "幼圆">华能信托舆情监控系统</font></p>
    <script>
        function sortrows(head, index){
            var value = parseInt(head.getAttribute("value"));
            head.setAttribute("value", 0 - value);
            var tbody = document.getElementById("tfhover");
            var rows = tbody.getElementsByTagName("tr");
            rows = Array.prototype.slice.call(rows, 1);
            rows.sort(function(row1, row2){
                var cell1 = row1.getElementsByTagName("td")[index];
                var cell2 = row2.getElementsByTagName("td")[index];
                var val1 = cell1.textContent || cell1.innerText;
                var val2 = cell2.textContent || cell2.innerText;
                var int1 = parseInt(val1);
                var int2 = parseInt(val2);
                if(int1 < int2){
                    return 0 - value;
                }
                else if(int1 > int2){
                    return value;
                }
                else{
                    return 0;
                }
            });
            for(var i = 0; i < rows.length; i++)
                tbody.appendChild(rows[i]);
        }
    window.onload=function(){
        var tfrow = document.getElementById('tfhover').rows.length;
        var tbRow=[];
        for (var i=1;i<tfrow;i++) {
            tbRow[i]=document.getElementById('tfhover').rows[i];
            tbRow[i].onmouseover = function(){
                this.style.backgroundColor = '#f3f8aa';
            };
            tbRow[i].onmouseout = function() {
                this.style.backgroundColor = '#ffffff';
            };
        }
    };
	//弹出隐藏层
	function ShowDiv(show_div,bg_div){
	 document.getElementById(show_div).style.display='block';
	 document.getElementById(bg_div).style.display='block' ;
	 var bgdiv = document.getElementById(bg_div);
	 bgdiv.style.width = document.body.scrollWidth; 
	 // bgdiv.style.height = $(document).height();
	 $("#"+bg_div).height($(document).height());
	};
	//关闭弹出层
	function CloseDiv(show_div,bg_div)
	{
	 document.getElementById(show_div).style.display='none';
	 document.getElementById(bg_div).style.display='none';
	};
    </script>
    <style type="text/css">
    table.tftable {font-size:12px;color:#333333;margin:auto;width:90%;border-width: 1px;border-color: #729ea5;border-collapse: collapse;}
    table.tftable th {font-size:14px;background-color:#acc8cc;border-width: 1px;padding: 8px;border-style: solid;border-color: #729ea5;text-align:center;}
    table.tftable tr {background-color:#ffffff;opacity:.88;}
    table.tftable td {font-size:12px;border-width: 1px;padding: 8px;border-style: solid;border-color: #729ea5;}
    ol{ 
    counter-reset: li;  
    list-style: none; 
    } 
    ol li{ 
    margin-top:5px; 
    } 

    ol a{ 
    font-family:微软雅黑; 
    font-size:14px; 
    text-decoration:none; 
    color:#000000; 
    } 
    ol a:before{ 
    content:counter(li); 
    counter-increment: li; 
    position:relative; 
    left:-5px; 
    width:15px; 
    height:15px; 
    line-height:15px; 
    text-align:center; 
    border:0px solid; 
    } 
    ol a:hover{ 
    color:red; 
    }
    #box-red { font-size:2vw;text-align:center;color:red;}
    #box-green { font-size:2vw;text-align:center;color:green;}
    #copyright{
	width:100%;
    background:#333333;
	text-align:center;
	height: 50px;
    padding-bottom:3px;
    color:white;
    font-family:KaiTi;
    font-size:16px;
    }
	.black_overlay{
	 display: none;
	 position: fixed;
	 top: 0%;
	 left: 0%;
	 width: 100%;
	 height: 100%;
	 background-color: black;
	 z-index:1001;
	 -moz-opacity: 0.8;
	 opacity:.80;
	 filter: alpha(opacity=80);
	}
	.white_content {
	 display: none;
	 position: fixed;
	 top: 10%;
	 left: 10%;
	 width: 80%;
	 height: 80%;
	 border: 16px solid lightblue;
	 background-color: white;
	 z-index:1002;
	 overflow: auto;
	}
	.white_content_small {
	 display: none;
	 position: fixed;
	 top: 20%;
	 left: 30%;
	 width: 40%;
	 height: 50%;
	 border: 16px solid lightblue;
	 background-color: white;
	 z-index:1002;
	 overflow: auto;
	}
	body 
	{
	background-image:"./img/bg1.jpg";
	background-repeat:no-repeat;
	background-attachment:fixed
	}
    </style>
</head>
<body background="./img/bg4.jpg">
    <?php
    require_once('./mysql_connect.php');
    connect(); //连接数据库
    echo "<br/>";
    echo "<table id='tfhover' class='tftable' border='1'>";
    echo "<tr><th>项目公司</th><th>主流网站信息</th><th value=1 onclick = 'sortrows(this, 2)'>当日评分</th><th value=1 onclick = 'sortrows(this, 3)'>本月评分</th></tr>";
    $sql = "set names utf8";
    mysql_query($sql);
    $myfile = fopen("showlist.txt", "r") or die("Unable to open file!");
    //$sql = "select distinct company from article";
    //$result_company = mysql_query($sql);
    $current_date0 = date("Y-m-d"); //当前日期(有前导0)
    $current_date = date("Y-n-j");  //当前日期(没有前导0)
    $days = date("j");                            //当月天数
    $current_month0 = substr($current_date0,0,strlen($current_date0)-2); //当前月
    $current_month = substr($current_date,0,strlen($current_date)-2);   //当前月
    //while($company = mysql_fetch_array($result_company,MYSQL_BOTH))
    while ($c = fgets($myfile))
    {
        //$c = $company['company']; //项目公司
		if (!feof($myfile))
		{
			$c=trim($c,"\r\n \xEF\xBB\xBF");
		}	
        $sql = "select * from article where (date = '$current_date' or date = '$current_date0') and (company like '$c%') and (score < 0)";
        $result = mysql_query($sql);
        echo "<tr><td align='center'><strong><font size='3' face='微软雅黑'>$c</font></strong></td><td>";   //填写项目公司
        $daily_score = 100;           //今日得分
        echo "<ol>";
        while($line = mysql_fetch_array($result,MYSQL_BOTH)) //填写信息
        {
            $daily_score += $line['score'];
            echo "<li><a href = '{$line['href']}' target='_blank'>{$line['title']}</a></li>";
        }
        if ($daily_score < 80)   //填写每日分数
            echo "</ol></td><td><div id='box-red'>$daily_score</div></td>";
        else
            echo "</ol></td><td><div id='box-green'>$daily_score</div></td>";
        $sql = "select * from article where (date like '$current_month%' or date like '$current_month0%') and (company like '$c%')";
        $result = mysql_query($sql);
        $month_score = 100*(int)$days;           //得分
        while($line = mysql_fetch_array($result,MYSQL_BOTH)) 
        {
            $month_score += $line['score'];
        }
        $month_score /= (int)$days;
        $month_score = round($month_score,1);//保留一位小数
		
        if ($month_score < 80)
            echo "<td><div id = 'box-red' onclick='ShowDiv(\"$c _MyDiv\",\"fade\")'>$month_score</div></td></tr>";
        else
            echo "<td><div id = 'box-green' onclick='ShowDiv(\"$c _MyDiv\",\"fade\")'>$month_score</div></td></tr>";
		echo "
		<div id='fade' class='black_overlay'>
		</div>
		<div id= '$c _MyDiv' class='white_content'>
			<div style='text-align: right; cursor: default; height: 40px;'>
				<span style='font-size: 16px;' onclick='CloseDiv(\"$c _MyDiv\",\"fade\")'>关闭</span>
			</div>
				<p style='text-align:center'>华小智 $current_month 月 $c 舆情监控报告</p>
			<ol>";
			$sql = "select * from article where (date like '$current_month%' or date like '$current_month0%') and (company = '$c') and (score < 0)";
			$result = mysql_query($sql);
			while($line = mysql_fetch_array($result,MYSQL_BOTH)) //填写信息
			{
				echo "<li><a href = '{$line['href']}' target='_blank'>{$line['title']}</a></li>";
			}
			echo"</ol>
		</div>";
    }
    fclose($myfile);
    echo "</table>";
    echo "<br/><br/>";
    echo "<div id='copyright'><br/>&copy;2018 <a href='http://www.huaxiaozhi.com' target='_blank'><img src='img/logo1.ico' height='18px' style='margin-bottom:-3px;'></a>华小智 版权所有</div>";
	?>
</table>

</body>
</html>