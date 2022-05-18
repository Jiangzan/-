window.onload=function (){
    //1.获取需要的标签
    var pic = $("#ad").children(".pic");
    var content = $(".content");
    var image = content.children("img");
    var slider_ctl=pic.children(".slider_ctl");
    var slider_ul=$(".index");

    var iNow=0;
    //2.动态创建指示器
    for(var i=0;i<image.length;i++){
        var li=document.createElement("li");
        li.className="li";
        slider_ul.append(li);

    }

    //3.让第一个选中
    slider_ul.children("li")[0].className="li current";

    //4.让滚动的内容归位
    var scroll_w = $(".pic")[0].offsetWidth;
    for(var i=1;i<image.length;i++){
        image[i].style.left=scroll_w+"px";
    }

    //5. 遍历监听操作
    var slider_ctl_child = slider_ctl.children("*");
    for(var i=0;i<slider_ctl_child.length;i++){
        //5.1监听事件
        slider_ctl_child[i].onmousedown=function (){
            if (this.className==="left"){//左边
                image[iNow].style.left=scroll_w+"px";
                iNow--;
                if (iNow<0) {iNow=image.length-1;}
                image[iNow].style.left=0;
                slider_ul.children("li").eq(iNow).css("background-color","red")
                   .siblings().css("background-color","rgba(100,100,100,0.3)");
            }else if (this.className==="right"){//右边
                image[iNow].style.left=scroll_w+"px";
                iNow++;
                if (iNow===image.length) {iNow=0;}
                image[iNow].style.left=0;
                slider_ul.children("li").eq(iNow).css("background-color","red")
                   .siblings().css("background-color","rgba(100,100,100,0.3)");
            }else{
                $("li.li").mouseover(function(){
                $(this).css("background-color","red")
                       .siblings().css("background-color","rgba(100,100,100,0.3)");
                image[iNow].style.left=scroll_w+"px";
                iNow = $(this).index();
                image[iNow].style.left=0;
            })
            }
        }
    }

    //自动轮播
    $(function(){
        //每个固定的时间转换图片
        var timer = setInterval(picLoop,1000);
            function picLoop(){
                image[iNow].style.left=scroll_w+"px";
                iNow++;
                if (iNow === slider_ul.children("li").length) {iNow=0;}
                image[iNow].style.left=0;
                slider_ul.children("li").eq(iNow).css("background-color","red")
                       .siblings().css("background-color","rgba(100,100,100,0.3)");
            }
              //定时器的控制
            $(".pic").hover(function(){
                clearInterval(timer);
                $(".left").show();
                $(".right").show();
            },function(){
                timer = setInterval(picLoop,1000);
                $(".left").hide();
                $(".right").hide();
            })
         })
}