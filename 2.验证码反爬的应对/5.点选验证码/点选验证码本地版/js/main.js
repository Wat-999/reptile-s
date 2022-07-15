

//随机词汇表
let arr=["新春快乐","阖家快乐","恭贺新禧","万事如意","张灯结彩","恭喜发财","假期愉快","今晚吃鸡"];
//创建随机成语
let math=arr[Math.floor(Math.random()*(arr.length-1))];

$('#minbox').html(`请依次点击图中的: <span>${math}</span>`)

//创建一个位置数组
let place=[{left:'0px',top:'0px'},{left:'200px',top:'0px'},{left:'0px',top:'100px'},{left:'200px',top:'100px'}]

// var left=Math.floor(Math.random()*(boxs[0].offsetWidth-51)) ;
// 			var top=Math.floor(Math.random()*(boxs[0].offsetHeight-51));

//随机打乱位置数组
place.sort(()=>{
	return Math.random()-0.5
})
console.log(place)

//创建一个数组用于与最终结果验证
let verify=[]

//遍历随机成语并创建标签
for(i in math){
	
	verify.push(i)
	//创建随机左边位置
	let left=Math.floor(Math.random()*(150))
	let top=Math.floor(Math.random()*(50));
	
	//创建存放span的div对象
	divs=$('<div class="fl"></div>')
	//给div定位
	divs.css({
		left:place[i].left,
		top:place[i].top
	})
	
	
	//创建储存文字的span标签
	span=$(`<span>${math[i]}</span>`)
	//随机span的位置
	span.css({
		left:left+'px',
		top:top+'px'
	})
	
	span.data('index',i);
	span.data('judge','true');
	divs.append(span);
	$('#box').append(divs)
	
}

//span点击事件
let cspan=[]
$('#box .fl span').click(function(){
	if($(this).data('judge')=='true'){
		cspan.push($(this).data('index'))
		$(this).data('judge','false')
		console.log(cspan)
		
	}else{
		console.log('重复点击')
	}
	
	
})

let a=0
//大盒子点击事件,用于生成小绿点
$('#box').click(function(event){
	a++
	
	let rad=$(`<div class='radio'>${a}</div>`)
	rad.css({
		left:event.pageX-$(this).offset().left-15+'px',
		top:event.pageY-$(this).offset().top-15+'px'
	})
	console.log(event.offsetX)
	
	$(this).append(rad)
	if(a==4){
		
		if(cspan.join()==verify.join()){
			
			$('#minbox').addClass('size')
			$('#minbox').html('验证成功')
			
			$('.fl').css('display','none')
			$('.radio').css('opacity','0')
			
			// setInterval(()=>{
			// 	location.reload()
			// },2000)
			
		}else{
			$('.fl').css('display','none')
			$('.radio').css('opacity','0')
			$('#minbox').html('验证失败')
			$('#minbox').css('color','red')
			setInterval(()=>{
				location.reload()
			},1000)
			
		}
		a=0
	}
	
	
	
	
})