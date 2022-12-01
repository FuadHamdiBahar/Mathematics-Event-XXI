// js fuad
const starttime = document.getElementById('showtime')
const countdown = document.getElementById('countdown')
const jstime = Date.parse(starttime.textContent)

setInterval(()=> {
  const now = new Date().getTime()
  const diff = jstime - now

  const d = Math.floor(jstime / (1000 * 60 * 60 * 24) - (now / (1000 * 60 * 60 * 24))) 
  const h = Math.floor(jstime / (1000 * 60 * 60) - (now / (1000 * 60 * 60))) % 24
  const m = Math.floor(jstime / (1000 * 60) - (now / (1000 * 60))) % 60
  const s = Math.floor(jstime / (1000) - (now / (1000))) % 60
  // console.log(h + ' : '+ m + ' : ' + s)
  
  console.log(diff);
  if(diff > 0) {
    countdown.innerHTML =  m + " menit " + s + " detik"
  } else {
    const forms = document.getElementById('form_ujian')

    document.getElementById("form_ujian").submit();
  }

},1000)


