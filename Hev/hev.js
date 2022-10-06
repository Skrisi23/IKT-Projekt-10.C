function szamol()
{
    var indulo=document.getElementById("select1").value;
    var érkezo=document.getElementById("select2").value;
    
    var eredmeny=indulo-érkezo;
if (indulo==érkezo){

    alert("Hiba:azonos megállokat választani");
    
}
else{
    alert("Menetidő:"+Math.abs(eredmeny)+"perc!")
}

}