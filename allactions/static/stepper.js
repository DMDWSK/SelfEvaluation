function hideStage(stage){
	// you can validate here
	$('#stage'+stage).removeClass('active');
	$('#stage-'+stage+'-step').addClass('done');
}

function showStage(stage) {
	$('#stage'+stage).removeClass('done');
	$('#stage-'+stage+'-step').removeClass('done');
	$('#stage'+stage).addClass('active');
	$('#stage-'+stage+'-step').addClass('active');



}

function removeActiveStage(stage) {
	$('#stage'+stage).removeClass('active');
	$('#stage-'+stage+'-step').removeClass('active');
	$('#stage'+stage).removeClass('done');
	$('#stage-'+stage+'-step').removeClass('done');
}

$(document).ready(function(){
	
})

