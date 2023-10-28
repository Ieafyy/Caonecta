$(document).ready(function() {

    let regex = /^\d+$/

    $("#ini").click(() => {
        $('#pagina-init').fadeOut(500, () => {
            $('#inputs').fadeIn(500)
        })
    })

    $("#btn").click(sender)

    $("#ret").click(() => {
        $('#outputs').fadeOut(500, () => {
            $('#inputs').fadeIn(500)
        })
    });

    $('#data').change(() => {
        console.log($('#data').val())
        if($('#data').val() == "") $('#seg-part').fadeOut(500)
        else $('#seg-part').fadeIn(500)
    })

    $('#cpequenos, #cgrandes').on('input', () => {
        console.log($('#cgrandes').val())
        
        let pequenos = $('#cpequenos').val()
        let grandes = $('#cgrandes').val()

        if(pequenos >= 0 && grandes >= 0 && regex.test(pequenos) && regex.test(grandes) && pequenos + grandes > 0) {
            $('#btn').removeAttr('disabled')
            $('#btn').removeClass('bg-gray-400')
            $('#btn').addClass('bg-sky-300 hover:bg-sky-400')
        }

        else{
            $('#btn').attr('disabled', 'disabled')
            $('#btn').removeClass('bg-sky-300 hover:bg-sky-400')
            $('#btn').addClass('bg-gray-400')
        } 
    })

});

function sender(){

    $.ajax({
        url: 'http://127.0.0.1:5000/dataget', 
        type:'POST', 
        data: {
            dt: $('#data').val(),
            ncg: $('#cgrandes').val(),
            ncp: $('#cpequenos').val()
        },
        success: (e) => {
            console.log(e)

            let petshop_e = e.nome 
            let valor_e = e.valor_dia
            let dist_e = e.distancia
            let dia_s = e.dia_semana

            $('#petshop-nome').text(petshop_e)
            $('#petshop-valor').text(valor_e.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' }))
            $('#petshop-dist').text(dist_e + 'Km')
            let data_pesq = $('#data').val().split('-')
            let data_format = data_pesq[2] + '/' + data_pesq[1] + '/' + data_pesq[0]
            $('#petshop-dia').text(dia_s + ' dia ' + data_format)
            $('#inputs').fadeOut(500, () => {
                $('#outputs').fadeIn(500)
            })
        }
    });
}

