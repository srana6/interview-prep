function getRandom(){
	var nl = Math.sqrt(Math.random() * 100);
	var n2 = (Math.floor(nl) % 4) + 1;
	return n2 + 1;
}


console.log(getRandom());