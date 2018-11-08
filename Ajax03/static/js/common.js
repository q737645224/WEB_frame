/**
 * Created by tarena on 18-11-6.
 */
function getxhr() {
            if (window.XMLHttpRequest){
                var xhr = new XMLHttpRequest()
            }else {
                var xhr = new Microsoft.ActiveXObject('Microsoft.XMLHTTP')
            }
            return xhr
        }