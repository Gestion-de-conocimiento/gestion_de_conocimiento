import axios from "axios";

export class Cargador {
    constructor(){
      this.form_data = {};
      this.imagenesVistaPrevia = [];
      this.contadorImagen = 0;
      this.imagenesAEliminar = [];
      this.ultimaImagenEnPreguntaAEditar = 0;
      this.imagenes = [];
    }
  
    onChange(e){			
      const file = e.target.files[0];
      let url = URL.createObjectURL(file);
      let imgp = document.getElementById("imgp");
      this.imagenes.push(file);
      this.acomodarImagen(url, 0, null);
    }
  
    async acomodarImagen(imagen, vaAEliminarse, idImagen) {
        if (vaAEliminarse === 1) {
            await this.imagenesVistaPrevia.push({
                imagen: imagen,
                id: this.contadorImagen,
                eliminar: true,
                idImagen: idImagen
            });
            this.contadorImagen++;
        } else {
            await this.imagenesVistaPrevia.push({
                imagen: imagen,
                id: this.contadorImagen
            });
            this.contadorImagen++;
        }
    }
    
    remove(imagen) {
        let i = this.imagenesVistaPrevia.indexOf(imagen);
        if (imagen.hasOwnProperty('eliminar')) {
            this.imagenesAEliminar.push(imagen);
        } else {
            this.imagenes.splice(i, 1);
        }
        this.imagenesVistaPrevia.splice(i, 1);

    }

  
    drop(event) {
        event.preventDefault();
        let self = this
        for (let i = 0; i < event.dataTransfer.files.length; i++) {
            let reader = new FileReader();
            reader.readAsDataURL(event.dataTransfer.files[i]);
            this.imagenes.push(event.dataTransfer.files[i]);
            reader.onload = function () {
                self.acomodarImagen(reader.result, 0, null);
            };
        }
        event.currentTarget.style.backgroundColor = 'white';
    }
  
    dragover(event) {
        event.preventDefault();
        event.currentTarget.style.backgroundColor = 'green';
    }
    
    dragleave(event) {
        event.currentTarget.style.backgroundColor = 'white';
    }
              
    async subirImagenes(id) {
        let extension = "";
        let ruta = "/subirr";
        let numeroPregunta = id;
        let nombreImagen = "";
        let alias = "";
        if (this.modoEdicion === 1) {
            let conteoActualImagenes = parseInt(this.ultimaImagenEnPreguntaAEditar) + 1;
            if (this.imagenes.length > 0) {
                for (let i = 0; i < this.imagenes.length; i++) {
                    extension = this.imagenes[i].name.split('.')[1];
                    nombreImagen = new Date().getTime() + "_" + i + "." + extension;
                    alias = "imagen_pregunta_" + numeroPregunta + "_" + (conteoActualImagenes) + "." +
                        extension;
                    this.form_data = new FormData();
                    this.form_data.append('imagen', this.imagenes[i]);
                    this.form_data.append('csrf-token', "{{ csrfToken }}");
                    this.form_data.append('alias', alias);
                    this.form_data.append('nombreImagen', nombreImagen);
                    this.form_data.append('idPregunta', id);
                    await axios.post(ruta, this.form_data).then((res) => {
                        console.log("La subida se ha completado con exito");
                    }).catch(function (error) {
                        console.log(error);
                    });
                    conteoActualImagenes++;
                }
            }
        } else {
            if (this.imagenes.length > 0) {
                for (let i = 0; i < this.imagenes.length; i++) {
                    extension = this.imagenes[i].name.split('.')[1];
                    nombreImagen = new Date().getTime() + "_" + i + "." + extension;
                    alias = "imagen_pregunta_" + numeroPregunta + "_" + (i + 1) + "." + extension;
                    this.form_data = new FormData();
                    this.form_data.append('imagen', this.imagenes[i]);
                    this.form_data.append('csrf-token', "{{ csrfToken }}");
                    this.form_data.append('alias', alias);
                    this.form_data.append('nombreImagen', nombreImagen);
                    this.form_data.append('idPregunta', id);
                    await axios.post(ruta, this.form_data).then((res) => {
                        console.log("La subida se ha completado con exito");
                    }).catch(function (error) {
                        console.log(error);
                    });
                }
            }
        }
        return true
    }

    async subirImagen(nombreImg){
   
        let extension = "";
        let ruta = "/subirr2";
        let nombreImagen = "";
        let alias = "";
        if (this.imagenes.length > 0) {
            for (let i = 0; i < this.imagenes.length; i++) {
                extension = this.imagenes[i].name.split('.')[1];
                nombreImagen = new Date().getTime() + "_" + i + "." + extension;
                if(i<10){
                    alias = nombreImg + "_0" + (i+1);
                }else{
                    alias = nombreImg + "_" + (i+1);
                }
                this.form_data = new FormData();
                this.form_data.append('imagen', this.imagenes[i]);
                this.form_data.append('csrf-token', "{{ csrfToken }}");
                this.form_data.append('alias', alias);
                this.form_data.append('nombreImagen', nombreImagen);
                await axios.post(ruta, this.form_data).then((res) => {
                    console.log("La subida se ha completado con exito");
                }).catch(function (error) {
                    console.log(error);
                });
            }
        }
    }
}


export default Cargador