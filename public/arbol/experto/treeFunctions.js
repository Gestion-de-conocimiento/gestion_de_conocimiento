    function close_rename_node_modal() {
      closeModal();
    }

    function close_create_node_modal() {
      closeModal();
    }

    function close_delete_parent_node_modal() {
      closeModal();
    }

    function close_create_parent_node_modal() {
      closeModal();
    }

    function close_delete_node_modal() {
      closeModal();
    }

    function rename_node() {
      let hasDuplicated = false;

      var name = $('#RenameNodeName').val();

      var primer_char = name.charAt(0);
      var longitud = 90; //Longitud del nuevo nombre del tema en nodo
      if (name == "" || name.length > longitud || primer_char == '1' || primer_char == '2' || primer_char == '3' || primer_char == '4' || primer_char == '5' || primer_char == '6' || primer_char == '7' || primer_char == '8' || primer_char == '8' || primer_char == '9' || primer_char == '0') {

        $('#mensaje_3').text("Por favor ingresa un nombre valido")
      } else {

        if (node_to_rename && rename_node_modal_active) {

          name = $('#RenameNodeName').val();

          hasDuplicated = checkhasDuplicated(name, node_to_rename.id);



          if (hasDuplicated) {
            swal({
                title: "Ya existe un nodo llamado así",
                text: "¿Esta seguro que desea renombrar el nodo actual?",
                icon: "warning",
                buttons: true,
                dangerMode: true,
              })
              .then((willDelete) => {
                if (willDelete) {
                  node_to_rename.name = name;
                  node_to_rename.textPosition = textPosition ? 1 : 0;
                  rename_node_modal_active = false;
                  textPosition = false;
                  saveNewName(node_to_rename)
                }

                $('#RenameNodeModal').modal('hide');

                outer_update(node_to_rename);
              });
          }

          if (!hasDuplicated) {
            node_to_rename.name = name;
            rename_node_modal_active = false;
            node_to_rename.textPosition = textPosition ? 1 : 0;
            textPosition = false;
            saveNewName(node_to_rename)
          }

        }

        if (!hasDuplicated) {

          //closeModal();
          $('#RenameNodeModal').modal('hide');
          outer_update(node_to_rename);
        }

      }

    }


    async function saveNewName(node_to_rename) {
      await axios({
        method: 'post',
        url: "http://67.207.86.184/tema/editarNodo/" + node_to_rename.id + "?id_nodo=" + node_to_rename.id + "&nombre_nodo=" + node_to_rename.name + "&textPosition=" + node_to_rename.textPosition,
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        data: {
          id_nodo: node_to_rename.id,
          nombre_nodo: node_to_rename.name,
          textPosition: node_to_rename.textPosition,
        }
      }).then(function(response) {
        //console.log("EDITADO")
      }).catch(function(error) {
        console.log('Error: ' + error)
      })
    }

    function generateUUID() {
      var d = new Date().getTime();
      var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (d + Math.random() * 16) % 16 | 0;
        d = Math.floor(d / 16);
        return (c == 'x' ? r : (r & 0x3 | 0x8)).toString(16);
      });
      return uuid;
    };

    function createNodesList(tree_rootAux, level, ignore) {

      if (ignore != null) {
        if (tree_rootAux['id'] == ignore['id']) {
          return
        }
        nodesToListToDelete.push({
          id: tree_rootAux['id'],
          name: tree_rootAux['name']
        });
      } else {
        nodesToList.push({
          id: tree_rootAux['id'],
          name: tree_rootAux['name']
        });
      }

      tree_rootAux['level'] = level;
      if (tree_rootAux['children'] != undefined) {
        for (var i = 0; i < tree_rootAux['children'].length; i++) {
          createNodesList(tree_rootAux['children'][i], i, ignore)
        }
      }
      if (level == 1) {
        tree_root = tree_rootAux;
      }
    }

    function updateNodeToList() {

      var select = document.getElementById("nodesSelect");
      var options = document.getElementById("nodesSelect").selectedIndex;
      var nodesSelectAllDelete = document.getElementById("nodesSelectAllDelete");
      var op2 = document.getElementById("nodesSelectAllDelete").selectedIndex;

      $('#nodesSelect').empty().trigger("change");
      $('#nodesSelectAllDelete').empty().trigger("change");
      nodesToList = [];
      createNodesList(tree_root, 1, null);
      //console.log(options)
      /*if(options!=-1)
   		$('nodesSelect').select2('data', null);
		if(op2!=-1)
    $('#nodesSelectAllDelete').select2('data', null);*/

      for (var i = 0; i < nodesToList.length; i++) {
        var nameNode = nodesToList[i].name;
        var idNode = nodesToList[i].id;
        var el = document.createElement("option");
        el.textContent = nameNode;
        el.value = idNode;
        //nodesSelectAllDelete.appendChild(el);
        //select.appendChild(el);
      }

    }


    function updateNodeToListToDelete() {

      var select = document.getElementById("nodesSelectAllDelete");
      var op = document.getElementById("nodesSelectAllDelete").selctedIndex;
      $('#nodesSelectAllDelete').empty().trigger("change");
      nodesToListToDelete = [];
      createNodesList(tree_root, 1, node_to_delete);
      //console.log(op+" "+157)
      //if(op!=-1 && op != null)
      //$('#nodesSelectAllDelete').select2('data', null);
      for (var i = 0; i < nodesToListToDelete.length; i++) {
        var nameNode = nodesToListToDelete[i].name;
        var idNode = nodesToListToDelete[i].id;
        var el = document.createElement("option");
        el.textContent = nameNode;
        el.value = idNode;
        select.appendChild(el);
      }

    }

    function isFamily(nodeParent, nodeSon) {
      if (nodeParent['name'] == nodeSon['name']) {
        return true;
      }
      if (nodeParent['children'] != undefined) {
        for (var i = 0; i < nodeParent['children'].length; i++) {
          if (isFamily(nodeParent['children'][i], nodeSon)) {
            return true;
          }
        }
      }
      return false;
    }

    function createParentConection() {

      var color = document.getElementById("colorConexion").value;

      color = color.slice(1);

      outer_update(tree_root);
      var op = document.getElementById('nodesSelect').options;
      var i = document.getElementById('nodesSelect').selectedIndex;
      var nodeSelected = $('#nodesSelect').select2('data')

      var nodeSelected = op[i].value;
      var couplingParent = tree_d3.nodes(tree_root).filter(function(d) {
        return d['id'] == nodeSelected;
      })[0];

      var couplingChild = tree_d3.nodes(tree_root).filter(function(d) {
        return d['id'] === create_parent_relation['id'];
      })[0];
      let isFamily1 = false;
      if (couplingParent['level'] > couplingChild['level']) {
        isFamily1 = isFamily(couplingChild, couplingParent)
      }
      if (couplingParent.children) {
        couplingParent.children.forEach(function(d) {
          if (d.id == couplingChild.id) {
            isFamily1 = true;
          }
        });
      }
      multiParents.forEach(function(d) {
        if ((d.parent.id == couplingParent.id && d.child.id == couplingChild.id) || (d.parent.id == couplingChild.id && d.child.id == couplingParent.id)) {
          isFamily1 = true;
        }
      });
      if (!isFamily1) {
        multiParents.push({
          parent: couplingParent,
          child: couplingChild
        })
        registerParentConection(couplingParent, couplingChild, color);
        //closeModal();
        $('#NewParentModal').modal('hide');
        outer_update(create_parent_relation);
      } else {
        alert("Son familia")
      }

    }

    function registerParentConection(parent, child, color) {
      axios({
        method: 'post',
        url: "http://67.207.86.184/tema/addsecundario?id_padre=" + parent.id + "&id_hijo=" + child.id + "&color=" + color,
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        data: {
          id_padre: parent.id,
          id_hijo: child.id,
          color: color
        }
      }).then(function(response) {

      }).catch(function(error) {
        console.log('Error: ' + error)
      })

    }

    function deleteParent() {
      create_node_parent['id']
      var op = document.getElementById('deleteParentSelect').options;
      var i = document.getElementById('deleteParentSelect').selectedIndex;
      //if(op!=-1)
      //var nodeSelected = $('#deleteParentSelect').select2('data')

      /*var index = -1;
      for (var x = 0; x < multiParents.length; x++) {
          let child = multiParents[x].child;
          let parent = multiParents[x].parent;
          if (child['id'] == create_node_parent['id']) {
              if (parent['id'] == op[i].value) {
                  //deleteParentDB(child, parent)
                  index = x;
                  break;
              }
          }
      }*/

      for (var x = 0; x < lista_nodos_eliminar.length; x++) {
        if (op[i].value == lista_nodos_eliminar[x].id_padre) {
          //console.log(lista_nodos_eliminar[x].id_padre, lista_nodos_eliminar[x].id_hijo, lista_nodos_eliminar[x].tipo);
          deleteParentDB(lista_nodos_eliminar[x].id_hijo, lista_nodos_eliminar[x].id_padre, lista_nodos_eliminar[x].tipo);
        }
      }

      /*if (index >= 0) {
          multiParents.splice(index, 1);
          closeModal();
          outer_update(tree_root);
      }*/


    }

    async function deleteParentDB(child, parent, tipo) {
      var tipo_numerico = 1;
      if (tipo == "secundarias") {
        tipo_numerico = 2;
      }

      await axios({
        method: 'post',
        url: "http://67.207.86.184/tema/deleteNodoSecundario?id_hijo=" + child + "&id_padre=" + parent + "&tipo=" + tipo_numerico,
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        data: {
          id_hijo: child.id,
          id_padre: parent.id,
          tipo: tipo_numerico
        }
      }).then(function(response) {
        //console.log("funciono");
        //console.log(response)
        //location.reload();
        window.location.href = "http://67.207.86.184/grafo";
      }).catch(function(error) {
        console.log('Error: ' + error)
      })
    }

    function create_node() {
      name = $('#CreateNodeName').val();

      var primer_char = name.charAt(0);
      var longitud = 90; //Longitud de caracteres para el nombre del nodo

      if (name == "" || name.length > longitud || primer_char == '1' || primer_char == '2' || primer_char == '3' || primer_char == '4' || primer_char == '5' || primer_char == '6' || primer_char == '7' || primer_char == '8' || primer_char == '8' || primer_char == '9' || primer_char == '0') {
        $('#mensaje_4').text("Por favor ingresa un nombre valido, el nombre no debe empezar con número ni tener más de 90 caracteres.")
      } else {

        let hasDuplicated = checkhasDuplicated(name, null);

        if (hasDuplicated) {
          swal({
              title: "Ya existe un nodo llamado así",
              text: "¿Esta seguro que desea crear nuevo el nodo?",
              icon: "warning",
              buttons: true,
              dangerMode: true,
            })
            .then((willDelete) => {
              if (willDelete) {
                confirmCreateNode(name)
              }

            });
        } else {
          confirmCreateNode(name)
        }
      }
    }


    async function confirmCreateNode(name) {
      if (create_node_parent && create_node_modal_active) {
        if (create_node_parent._children != null) {
          create_node_parent.children = create_node_parent._children;
          create_node_parent._children = null;
        }
        if (create_node_parent.children == null) {
          create_node_parent.children = [];
        }
        //  id = generateUUID();

        //debugger;
        new_node = {
          'name': name,
          'id': 0,
          'depth': create_node_parent.depth + 1,
          'level': create_node_parent['level'] + 1,
          'level2': create_node_parent['level2'] + 1,
          'freex': create_node_parent['freex'],
          'freey': create_node_parent['freey'] + 100,
          'children': [],
          'textPosition': textPosition ? 1 : 0,
          '_children': null
        };

        textPosition = false;
        var newId = await createRequestNewNode(new_node);

        new_node['id'] = newId;
        create_node_parent.children.push(new_node);

        create_node_modal_active = false;
        $('#CreateNodeName').val('');

      }
      //closeModal();
      $('#CreateNodeModal').modal('hide');
      outer_update(create_node_parent);
    }


    function checkhasDuplicated(name, id) {
      for (var i = 0; i < nodesToList.length; i++) {
        if ((nodesToList[i].name == name && nodesToList[i].id != id)) {
          return true;
        }
      }
      return false;
    }





    function visit(parent, visitFn, childrenFn) {
      if (!parent) return;

      visitFn(parent);

      var children = childrenFn(parent);
      if (children) {
        var count = children.length;
        for (var i = 0; i < count; i++) {
          visit(children[i], visitFn, childrenFn);
        }
      }
    }

    function makeListSons(node) {
      var nodesSelectAllDelete = document.getElementById("nodesSelectChildNewParent");
      var op = document.getElementById("nodesSelectChildNewParent").selectedIndex;

      $('#nodesSelectChildNewParent').empty().trigger("change");
      //console.log(op+"Selecciona");
      //if(op!=-1)
      //$('#nodesSelectChildNewParent').select2('data', null);

      if (node.children != null) {
        for (var i = 0; i < node.children.length; i++) {
          var nameNode = node.children[i].name;
          var idNode = node.children[i].id;
          var el = document.createElement("option");
          el.textContent = nameNode;
          el.value = idNode;
          nodesSelectChildNewParent.appendChild(el);
        }
      }
    }

    function delete_node(node1) {
      var op = document.getElementById('optionsDelete').options;
      var index = document.getElementById('optionsDelete').selectedIndex;
      //console.log(op[index].index+" opciones")

      let deleteOption = op[index].index + 1



      let permiteDelete = true;

      if (node1.children != undefined) {
        permiteDelete = false;

        if (deleteOption == 1) {
          //console.log("Entra aquí");
          swal({
              title: "Este nodo tiene hijos",
              text: "¿Esta seguro que desea eliminar el nodo?",
              icon: "warning",
              buttons: true,
              dangerMode: true,
            })
            .then((willDelete) => {
              if (willDelete) {
                confirmDeleteNode(node1);
                deleteAllSons(node1.id);
              }
            });
        } else if (deleteOption == 2) {
          swal({
              title: "Este nodo tiene hijos",
              text: "¿Esta seguro que desea pasar los hijos al nodo abuelo?",
              icon: "warning",
              buttons: true,
              dangerMode: true,
            })
            .then((willDelete) => {
              if (willDelete) {
                let parent = node1.parent;

                for (var i = 0; i < node1['children'].length; i++) {
                  parent.children.push(node1.children[i]);
                }

                node1['children'] = null;
                deleteandcambiarPadre(node1, parent);

                confirmDeleteNode(node1);
                outer_update(parent);

              }
            });
        } else if (deleteOption == 3) {
          swal({
              title: "Este nodo tiene hijos",
              text: "¿Esta seguro que desea pasar los hijos a un nodo hijo?",
              icon: "warning",
              buttons: true,
              dangerMode: true,
            })
            .then((willDelete) => {
              if (willDelete) {
                let parent = node1.parent;
                let newChildParent = null;

                if (node1['children'] != undefined) {
                  //debugger;


                  //if(op2!=-1)
                  //var nodeSelectedS = $('#nodesSelectChildNewParent').select2('data');

                  var index = document.getElementById('nodesSelectChildNewParent').selectedIndex;
                  var op = document.getElementById('nodesSelectChildNewParent').options;

                  newChildParent = tree_d3.nodes(tree_root).filter(function(d) {

                    return d['id'] == op[index].value;

                  })[0];

                  newChildParent['freex'] = node1['freex']
                  newChildParent['freey'] = node1['freey']
                  if (newChildParent['children'] == undefined) {
                    newChildParent['children'] = [];
                  }


                  for (var i = 1; i < node1['children'].length; i++) {
                    newChildParent.children.push(node1.children[i]);
                  }
                }
                parent.children.push(newChildParent)

                node1['children'] = null;
                hacerHijoPadre(node1, newChildParent);
                confirmDeleteNode(node1);
                outer_update(parent);

              }
            });
        } else if (deleteOption == 4) {
          swal({
              title: "Este nodo tiene hijos",
              text: "¿Esta seguro que desea pasar los hijos al nodo seleccionado?",
              icon: "warning",
              buttons: true,
              dangerMode: true,
            })
            .then((willDelete) => {
              if (willDelete) {
                var index = document.getElementById('nodesSelectAllDelete').selectedIndex;
                var vec = document.getElementById('nodesSelectAllDelete').options;

                //console.log("Este es el index: "+vec[index].value);
                //if(index!=null)
                //var nodeSelectedS = $('#nodesSelectAllDelete').select2('data');


                var nodeSelected = tree_d3.nodes(tree_root).filter(function(d) {
                  //var index= document.getElementById('nodesSelectAllDelete').selectedIndex;
                  //var vec= document.getElementById('nodesSelectAllDelete').opciones;
                  return d['id'] == vec[index].value;
                })[0];
                //console.log("Esto es lo que retorna :"+nodeSelected)
                if (nodeSelected['children'] == undefined) {
                  nodeSelected['children'] = [];
                }

                for (var i = 0; i < node1['children'].length; i++) {
                  nodeSelected.children.push(node1.children[i]);
                }

                node1['children'] = null;
                deleteandcambiarPadre(node1, nodeSelected);

                confirmDeleteNode(node1);
                outer_update(nodeSelected);

              }
            });
        }
      }
      if (permiteDelete) {
        deleteAllSons(node1.id);
        confirmDeleteNode(node1);
      }

      $('#DeleteNodeModal').modal('hide');
      //closeModal();
    }

    function hacerHijoPadre(oldParent, newChildParent) {
      axios({
        method: 'post',
        url: "http://67.207.86.184/tema/hacerHijoPadre/" + oldParent.id + "?id=" + oldParent.id + "&id2=" + newChildParent.id,
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        data: {
          id: oldParent.id,
          id2: newChildParent.id
        }
      }).then(function(response) {
        //console.log("funciono")
      }).catch(function(error) {
        console.log('Error: ' + error)
      })
    }


    function cambiarPadre(nodeToChange, newParent) {
      axios({
        method: 'post',
        url: "http://67.207.86.184/tema/cambiarPadre/" + nodeToChange.id + "?id=" + nodeToChange.id + "&id2=" + newParent.id,
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        data: {
          id: nodeToChange.id,
          id2: newParent.id
        }
      }).then(function(response) {
        //console.log("funciono")
      }).catch(function(error) {
        console.log('Error: ' + error)
      })
    }

    function actualizarPadre(oldParent, newParent, children, color) {
      axios({
        method: 'post',
        url: "http://67.207.86.184/tema/cambiarPadre/" + oldParent + "?id=" + oldParent + "&id2=" + newParent + "&hijo=" + children + "&color=" + color,
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        data: {
          id: oldParent,
          id2: newParent,
          hijo: children,
          color: color
        }
      }).then(function(response) {
        //console.log(response)
        //console.log("funciono")
      }).catch(function(error) {
        console.log('Error: ' + error)
      })
    }

    function deleteandcambiarPadre(oldParent, newParent) {
      axios({
        method: 'post',
        url: "http://67.207.86.184/tema/deleteandcambiarPadre/" + oldParent.id + "?id=" + oldParent.id + "&id2=" + newParent.id,
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        data: {
          id: oldParent.id,
          id2: newParent.id
        }
      }).then(function(response) {
        //console.log("funciono")
      }).catch(function(error) {
        console.log('Error: ' + error)
      })
    }



    function deleteAllSons(idNode) {
      //debugger;
      axios({
        method: 'post',
        url: "http://67.207.86.184/tema/deleteTema1/" + idNode + "?id=" + idNode,
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        data: {
          id: idNode
        }
      }).then(function(response) {
        //console.log("funciono")
      }).catch(function(error) {
        console.log('Error: ' + error)
      })
    }

    function confirmDeleteNode(node1) {
      visit(tree_root, function(d) {
          if (d.children) {
            for (var child of d.children) {
              if (child == node1) {

                d.children = _.without(d.children, child);
                getAllNodesDeleted(node1);
                outer_update(tree_root);
                break;
              }
            }
          }
        },
        function(d) {
          return d.children && d.children.length > 0 ? d.children : null;
        });

      updateNodeToList();
    }


    function getAllNodesDeleted(node1) {
      var index = -1;
      for (var x = 0; x < multiParents.length; x++) {
        let child = multiParents[x].child;
        let parent = multiParents[x].parent;
        if (child['id'] == node1['id'] || parent['id'] == node1['id']) {
          index = x;
          break;
        }
      }

      if (index >= 0) {
        multiParents.splice(index, 1);
      }


      if (node1.children) {
        for (var x = 0; x < node1.children.length; x++) {
          getAllNodesDeleted(node1.children[x])
        }
      }
    }

    async function deleteNodeConfirm() {
      try {
        let result = await swal({
          title: 'Are you sure?',
          text: "You won't be able to revert this!",
          type: 'warning',
          showCancelButton: true,
          confirmButtonText: 'Yes, delete it!',
          cancelButtonText: 'No, cancel!',
          reverseButtons: true
        });
        // SUCCESS
        return result;
      } catch (e) {
        // Fail!
        console.error(e);
      }
    }


    function deleteRecursiveNode(node, nodeToDelete) {
      if (node['name'] == nodeToDelete['name']) {
        return true;
      }
      if (node['children'] != undefined) {
        for (var i = 0; i < node['children'].length; i++) {
          if (deleteRecursiveNode(node['children'][i], nodeToDelete)) {
            if (node['children'][i]['name'] == nodeToDelete['name']) {
              node.children = _.without(node.children, node['children'][i]);
            }
            return true;
          }
        }
      }
      return false;
    }

    async function updatePosition(draggingNode) {
      await axios({
        method: 'post',
        url: "http://67.207.86.184/tema/posicion?newx=" + draggingNode.freex + "&newy=" + draggingNode.freey + "&id=" + draggingNode.id,
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        data: {
          newy: draggingNode.freey,
          newy: draggingNode.freex,
          id: draggingNode.id
        }
      }).then(function(response) {
        //console.log("funciono")
      }).catch(function(error) {
        console.log('Error: ' + error)
      })
    }

    async function createRequestNewNode(new_node) {

      var color = document.getElementById("colorNuevaConexion").value;

      color = color.slice(1);

      var newId;
      await axios({
        method: 'post',
        url: "http://67.207.86.184/tema/addTema?nombre_tema=" + new_node.name + "&nivel_tema=" + (create_node_parent.level2 + 1) + "&id_padre=" + create_node_parent.id +
          "&freex=" + new_node.freex + "&freey=" + new_node.freey + "&textPosition=" + new_node.textPosition + "&color=" + color,
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        data: {
          nombre_tema: new_node.name,
          id_padre: create_node_parent.id,
          nivel_tema: create_node_parent.level2 + 1,
          freex: new_node.freex,
          freey: new_node.freey,
          textPosition: new_node.textPosition,
          color: color

        }
      }).then(function(response) {
        //debugger;
        newId = response['data']['newId']
      }).catch(function(error) {
        console.log('Error: ' + error)
      })
      return newId[0];

    }


    async function getTreeFromBD() {
      ////debugger;
      let treeData = null;
      treeExtraConections = null;
      let tree = null;

      //Consultar la base de datos
      await axios({
        method: 'get',
        url: "http://67.207.86.184/temas/arbol",
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
      }).then(function(response) {
        treeData = response['data']['treeStructure'];

        treeExtraConections = response['data']['extraParent'];
      }).catch(function(error) {
        console.log('Error: ' + error)
      });

      return treeData;
    }

    function createExtraConectionStructure(treeData) {
      var couplingParent = null;
      var couplingChild = null;
      treeExtraConections.forEach(function(d1) {
        couplingParent = tree_d3.nodes(treeData).filter(function(d) {
          return d['id'] == d1['id_padre'];
        })[0];
        couplingChild = tree_d3.nodes(treeData).filter(function(d) {
          return d['id'] == d1['id_hijo'];
        })[0];

        multiParents.push({
          parent: couplingParent,
          child: couplingChild,
        })
      });
    }



    function listarNodos(d) {
      let select = document.getElementById("nodesSelect");
      let nodos = [];
      let mensaje_uno = document.getElementById("mensaje_1");
      $('#nodesSelect').empty().trigger("change");
      mensaje_uno.innerHTML = "";
      axios({
        method: 'get',
        url: "http://67.207.86.184/temas/posiblesNodosPadres/" + d.level2,
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
      }).then(function(response) {
        nodos = response.data[0];
        for (var i = 0; i < nodos.length; i++) {
          if (nodos[i].id == d.id) {
            nodos.splice(i, 1)
          }
        }
        axios({
          method: 'get',
          url: "http://67.207.86.184/temas/obtenerPadres/" + d.id,
          headers: {
            'content-type': 'application/x-www-form-urlencoded'
          },
        }).then(function(response) {
          let padres = response.data[0];
          for (var j = 0; j < padres.length; j++) {
            for (var i = 0; i < nodos.length; i++) {
              if (nodos[i].id == padres[j].id_padre) {
                nodos.splice(i, 1)
              }
            }
          }
          for (var i = 0; i < nodos.length; i++) {
            var el = document.createElement("option");
            el.textContent = nodos[i].nombre_tema;
            el.value = nodos[i].id;
            select.appendChild(el);
          }
          if (nodos.length == 0) {
            mensaje_uno.innerHTML = "Ya no hay nodos candidatos a ser padre";
          }
        }).catch(function(error) {
          console.log('Error: ' + error)
        });
      }).catch(function(error) {
        console.log('Error: ' + error)
      });
    }

    function listarNodosPadre(d) {
      let select = document.getElementById("newParentSelect");
      let nodos = [];
      let mensaje_uno = document.getElementById("mensaje_1");
      $('#newParentSelect').empty().trigger("change");
      mensaje_uno.innerHTML = "";
      axios({
        method: 'get',
        url: "http://67.207.86.184/temas/posiblesNodosPadres/" + d.level2,
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
      }).then(function(response) {
        nodos = response.data[0];
        for (var i = 0; i < nodos.length; i++) {
          if (nodos[i].id == d.id) {
            nodos.splice(i, 1)
          }
        }
        axios({
          method: 'get',
          url: "http://67.207.86.184/temas/obtenerPadres/" + d.id,
          headers: {
            'content-type': 'application/x-www-form-urlencoded'
          },
        }).then(function(response) {
          let padres = response.data[0];
          for (var j = 0; j < padres.length; j++) {
            for (var i = 0; i < nodos.length; i++) {
              if (nodos[i].id == padres[j].id_padre) {
                nodos.splice(i, 1)
              }
            }
          }
          for (var i = 0; i < nodos.length; i++) {
            var el = document.createElement("option");
            el.textContent = nodos[i].nombre_tema;
            el.value = nodos[i].id;
            select.appendChild(el);
          }
          if (nodos.length == 0) {
            mensaje_uno.innerHTML = "Ya no hay nodos candidatos a ser padre";
          }
        }).catch(function(error) {
          console.log('Error: ' + error)
        });
      }).catch(function(error) {
        console.log('Error: ' + error)
      });

      var select_conexion = document.getElementById("oldParentSelect");
      $('#oldParentSelect').empty().trigger("change");
      axios({
        method: 'get',
        url: "http://67.207.86.184/obtenerConexiones/" + d.id,
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
      }).then(function(response) {
        let conexiones = response.data[0];

        for (var i = 0; i < conexiones.length; i++) {
          var el = document.createElement("option");
          el.textContent = conexiones[i].nombre_tema;
          el.value = conexiones[i].id_padre;
          select_conexion.appendChild(el);
        }

        if (conexiones.length == 0) {
          mensaje_uno.innerHTML = "Ya no hay nodos candidatos a ser padre";
        }
      }).catch(function(error) {
        console.log('Error: ' + error)
      });

    }

    async function obtenerColoresRelaciones() {

      let respuesta = [];
      let relaciones_primarias = [];
      let relaciones_secundarias = [];
      await axios({
        method: 'get',
        url: "http://67.207.86.184/tema/relacionesPrimarias",
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
      }).then(function(response) {
        for (var i = 0; i < response['data'].length; i++) {
          if (response['data'][i].tipo == "primarias") {
            relaciones_primarias.push(response['data'][i]);
          } else {
            relaciones_secundarias.push(response['data'][i]);
          }
        }
        respuesta.relacionesPrimarias = relaciones_primarias;
        respuesta.relacionesSecundarias = relaciones_secundarias;
      }).catch(function(error) {
        console.log('Error: ' + error)
      });
      return respuesta;
    }

    async function click_conexion(d) {
      /*console.log("Valor de x " + x_init);
      console.log("Valor de y " + y_init);
      console.log("Valor de e " + e_init);*/
      //$('#CambiarColorConexion').foundation('reveal', 'open');
      $('#CambiarColorConexion').modal('show');
      document.getElementById("idConexion").value = d.padre + "-" + d.hijo;
    }

    async function guardarNuevoColor() {
      var nuevo_color = document.getElementById("colorConexionNvo").value;
      var id_conexion = document.getElementById("idConexion").value;
      nuevo_color = nuevo_color.slice(1);
      await axios({
        method: 'post',
        url: "http://67.207.86.184/tema/actualizarColor?id=" + id_conexion + "&color=" + nuevo_color,
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        data: {
          id: id_conexion,
          color: nuevo_color
        }
      }).then(function(response) {
        outer_update(tree_root);
        //closeModal();
        $('#CambiarColorConexion').modal('hide');

      }).catch(function(error) {
        console.log('Error: ' + error)
      })

    }

    // Cambiar el tamaño de los nodos
    async function sizeNode() {
      //ratio = $('#slider').attr('data-slider');

      ratio = $('#slider').val();
      outer_update(tree_root);
    }

    // Cambiar el tamaño de los nodos
    async function updateSizeNode() {
      //ratio = $('#slider').attr('data-slider');

      ratio = $('#slider').val();

      await axios({
        method: 'post',
        url: "http://67.207.86.184/tema/actualizarRadio/" + ratio,
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        data: {
          radio: ratio
        }
      }).then(function(response) {
        //debugger;
        //console.log(response);
        /*console.log(ratio)
        console.log('SE ACTUALIZO')*/
        outer_update(tree_root);

      }).catch(function(error) {
        console.log('Error: ' + error)
      })

      outer_update(tree_root);
    }

    // Obtener el radio de la base de datos
    async function getSizeNode() {
      let respuesta;
      await axios({
        method: 'get',
        url: "http://67.207.86.184/tema/obtenerRadio",
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
      }).then(function(response) {
        //Obteniendo la data
        respuesta = response['data'][0];
        //Actualizando el radio
        ratio = respuesta[0]['radio']
        //Renderizando el arbol
        //outer_update(tree_root);


        //$('#slider').foundation('slider', 'set_value', ratio);
        $('#slider').val(ratio)

        //console.log(respuesta[0]['radio']);

      }).catch(function(error) {
        console.log('Error: ' + error)
      });

      return respuesta[0]['radio'];
    }



    var total_bueno = 0
    var total_regular = 0
    var total_bajo = 0
    var total = 0

    var id_tema = "";
    var evidencia = false;
    var total_nodos_evaluados = 0;
    var nodo_evaluado = false;

    function loadQuestions(d) {


      id_tema = d.id
      evidencia = false;

      for (var i = 0; i < nodos_ordenados.length; i++) {
        if (id_tema == nodos_ordenados[i]) {
          numero_nodo_ordenado = i;
          break
        }
      }


      if (numero_nodo_ordenado == 0) {
        document.getElementById("btn_anterior_tema").disabled = true;
      } else {
        document.getElementById("btn_anterior_tema").disabled = false;
      }

      if (numero_nodo_ordenado == (nodos_ordenados.length - 1)) {
        document.getElementById("btn_siguiente_tema").disabled = true;
      } else {
        document.getElementById("btn_siguiente_tema").disabled = false;
      }

      //nodos_ordenados[numero_nodo_ordenado]


      axios({
        method: 'get',
        url: "http://67.207.86.184/preguntas/nodo?id=" + id_tema,
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
      }).then(function(response) {


        $('#questionList').empty();
        $("#questionList").append('<p style="font-size:20px;"> Tema: <b> ' + response.data.banco_preguntas[0].nombre_tema + ' (' + (numero_nodo_ordenado + 1) + ' de ' + nodos_ordenados.length + ' ) </b> </p>');

        //$("#questionList").append('<p> Nodo: <b> '+ (numero_nodo_ordenado+1) +' de ' + nodos_ordenados.length+ ' </b> </p>');

        document.getElementById("btn_guardar_porcentajes").disabled = true;
        //console.log("Numero de evidencias "+ response.data.porcentajes.length );
        if (response.data.porcentajes.length > 0) {
          evidencia = true
          total_bueno = response.data.porcentajes[0].bueno
          total_regular = response.data.porcentajes[0].regular
          total_bajo = response.data.porcentajes[0].bajo

          $("#questionList").append('<p style="font-size:20px;"> Estado: <b> <span style="color:green"> Evaluado </span> </b> </p>');
          nodo_evaluado = true;

        } else {
          total_bueno = 0
          total_regular = 0
          total_bajo = 0

          $("#questionList").append('<p style="font-size:20px;"> Estado: <b> <span style="color:red"> No evaluado </span> </b> </p>');
          nodo_evaluado = false;
        }

        document.getElementById("inp_bueno").value = total_bueno;
        document.getElementById("inp_regular").value = total_regular;
        document.getElementById("inp_bajo").value = total_bajo;

        total = Number(total_bueno) + Number(total_regular) + Number(total_bajo);

        document.getElementById("lbl_total_porcentaje").innerHTML = total


        if (response.data.banco_preguntas[0].nivel > 1) {
          //$('#QuestionModal').foundation('reveal', 'open');

          $('#QuestionModal').modal('show');
        } else {
          swal({
            position: 'top-end',
            icon: 'warning',
            title: "No es necesario registrar las evidencias para este tema",
            showConfirmButton: false,
            timer: 1500
          })
        }

      }).catch(function(error) {
        console.log('Error: ' + error)
      });



    }

    var haCambiadoInput = false;

    async function cambioInput(id) {

      haCambiadoInput = true;

      totall = document.getElementById(id).value;

      totall = Math.trunc(Number(totall))
      document.getElementById(id).value = totall;
      if (Number(totall) > 100)
        document.getElementById(id).value = document.getElementById(id).value.charAt(0) + document.getElementById(id).value.charAt(1);



      if (id == "inp_bueno") {
        total_bueno = document.getElementById("inp_bueno").value;
        console.log(total_bueno)
        if (total_bueno == 0) {

          console.log("Ingresa numero mayor a 0")
          document.getElementById("msg_cero").innerHTML = "Ingrese número mayor a 0"
          document.getElementById("msg_cero").style.color = "red";
          document.getElementById("btn_guardar_porcentajes").disabled = true;
          bandera = true;
        } else {
          document.getElementById("msg_cero").innerHTML = ""
          bandera = false;
        }

      } else if (id == "inp_regular") {
        total_regular = document.getElementById("inp_regular").value;
        console.log(total_regular)
        if (total_regular == 0) {
          console.log("Ingresa numero mayor a 0")
          document.getElementById("msg_cero").innerHTML = "Ingrese número mayor a 0"
          document.getElementById("msg_cero").style.color = "red";
          document.getElementById("btn_guardar_porcentajes").disabled = true;
          bandera2 = true;
        } else {
          document.getElementById("msg_cero").innerHTML = ""
          bandera2 = false;
        }
      } else {
        total_bajo = document.getElementById("inp_bajo").value;
        console.log(total_bajo)
        if(total_bajo==0){
          console.log("Ingresa numero mayor a 0")
          document.getElementById("msg_cero").innerHTML = "Ingrese número mayor a 0"
          document.getElementById("msg_cero").style.color = "red";
          document.getElementById("btn_guardar_porcentajes").disabled = true;
          bandera3 = true;
        }else{
          document.getElementById("msg_cero").innerHTML = ""
          bandera3 = false;
        }
      }



      total = Number(total_bueno) + Number(total_regular) + Number(total_bajo)

      document.getElementById("lbl_total_porcentaje").innerHTML = total

       if (total != 100 ) {
        document.getElementById("msg_porcentaje").innerHTML = "La suma de los porcentajes debe ser 100"
        document.getElementById("msg_porcentaje").style.color = "red";
        document.getElementById("btn_guardar_porcentajes").disabled = true;
      } else if (bandera == true || bandera2 == true || bandera3==true) {
        document.getElementById("btn_guardar_porcentajes").disabled = true;
        document.getElementById("msg_cero").innerHTML = "Ingrese número mayor a 0"
        document.getElementById("msg_cero").style.color = "red";
        document.getElementById("msg_porcentaje").innerHTML = ""

      } 
      else {
        document.getElementById("btn_guardar_porcentajes").disabled = false;
        document.getElementById("msg_porcentaje").innerHTML = ""
        document.getElementById("msg_cero").innerHTML = ""

      }



    };

    async function guardarPorcentajes() {

      document.getElementById("btn_guardar_porcentajes").disabled = true;

      porcentaje_total = Number(total_bueno) + Number(total_bajo) + Number(total_regular)

      if (porcentaje_total == 100) {

        await axios({
          method: 'post',
          url: "http://67.207.86.184/temas/guardarProbabilidades",
          data: {
            bueno: total_bueno,
            regular: total_regular,
            bajo: total_bajo,
            id_tema: id_tema,
            evidencia: evidencia
          }
        }).then(function(response) {

          //console.log("ESTO ES LA RESPUESTA DEL GUARDADO");
          //console.log(response);

          var mensaje = ""
          if (evidencia == true) {
            mensaje = "Datos actualizados correctamente"
          } else {
            mensaje = "Datos almacenados correctamente"
            //total_evaluados
            total_nodos_evaluados = total_nodos_evaluados + 1
            document.getElementById("total_evaluados").innerHTML = " " + total_nodos_evaluados;
          }

          if (total_nodos_evaluados == nodos_ordenados.length) {
            swal({
              position: 'top-end',
              icon: 'success',
              title: "Ha terminado de registrar la evidencia de todos los temas",
              showConfirmButton: false,
              showCancelButton: false,

            })
          } else {

            swal({
              position: 'top-end',
              icon: 'success',
              title: mensaje,
              timer: 1500,
              showConfirmButton: false,
              showCancelButton: false,
              buttons: false
            })
          }

          haCambiadoInput = false
          evidencia = true;

          /*console.log("PRUEBAS");
          console.log(numero_nodo_ordenado);
          console.log( (nodos_ordenados.length - 1) );*/
          if (numero_nodo_ordenado == (nodos_ordenados.length - 1)) {
            comenzarRegistroEvidencia()

          } else {
            numero_nodo_ordenado = numero_nodo_ordenado + 1;
            siguienteNodoNoRegistrado();
            //comenzarRegistroEvidencia();

          }


          outer_update(tree_root);
        }).catch(function(error) {
          console.log('Error: ' + error)
        });


      } else {
        document.getElementById("msg_porcentaje").innerHTML = "Por favor, llene correctamente los porcentajes";
      }


    }

    async function siguienteNodoNoRegistrado() {
      axios({
        method: 'get',
        url: "http://67.207.86.184/preguntas/nodo?id=" + nodos_ordenados[numero_nodo_ordenado],
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
      }).then(function(response) {
        if (response.data.porcentajes.length > 0) {
          numero_nodo_ordenado = numero_nodo_ordenado + 1;

          if (total_nodos_evaluados == nodos_ordenados.length) {
            comenzarRegistroEvidencia();
          } else {
            siguienteNodoNoRegistrado();
          }
        } else {
          comenzarRegistroEvidencia();
        }
      }).catch(function(error) {
        console.log('Error: ' + error)
      });
    }

    async function obtenerEvidenciaExpertos() {

      var evidencia = []
      await axios({
        method: 'get',
        url: "http://67.207.86.184/obtenerEvidencias",
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
      }).then(function(response) {
        evidencia = response.data[0]

        total_nodos_evaluados = evidencia.length
        document.getElementById("total_evaluados").innerHTML = " " + evidencia.length;
      }).catch(function(error) {
        console.log('Error: ' + error)
      });


      return evidencia;
    }


    var numero_nodo_ordenado = 0

    function resetearFormulario() {

      document.getElementById("inp_bueno").value = 0;
      document.getElementById("inp_regular").value = 0;
      document.getElementById("inp_bajo").value = 0;
      total_bueno = 0
      total_regular = 0
      total_bajo = 0

      total = Number(total_bueno) + Number(total_regular) + Number(total_bajo)

      document.getElementById("lbl_total_porcentaje").innerHTML = total
      document.getElementById("msg_porcentaje").innerHTML = ""
      document.getElementById("msg_cero").innerHTML = ""
      document.getElementById("btn_guardar_porcentajes").disabled = true;

      if (numero_nodo_ordenado == 0) {
        document.getElementById("btn_anterior_tema").disabled = true;
      } else {
        document.getElementById("btn_anterior_tema").disabled = false;
      }

      if ((numero_nodo_ordenado + 1) == nodos_ordenados.length) {
        document.getElementById("btn_siguiente_tema").disabled = true;
      } else {
        document.getElementById("btn_siguiente_tema").disabled = false;
      }
    }

    var primero = true;

    async function resetearConteo() {

      //$('html, body').animate({ scrollTop: 0 }, 'fast');
      if (total_nodos_evaluados == nodos_ordenados.length) {


        swal({
          position: 'top-end',
          icon: 'success',
          title: "Ha terminado de registrar la evidencia de todos los temas",
          showConfirmButton: false,
          showCancelButton: false,

        })

      } else {
        $('#modalDeCarga').modal('show');
        numero_nodo_ordenado = 0;
        encontrarPrimero()
      }

    }

    async function encontrarPrimero() {


      axios({
        method: 'get',
        url: "http://67.207.86.184/preguntas/nodo?id=" + nodos_ordenados[numero_nodo_ordenado],
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
      }).then(function(response) {

        //console.log("Nivel del tema " + response.data.banco_preguntas.nivlel);

        if (response.data.porcentajes.length > 0) {
          //console.log("Ya esta evaluado");
          numero_nodo_ordenado = numero_nodo_ordenado + 1;
          encontrarPrimero()
        } else {
          $('#modalDeCarga').modal('hide');
          $('#QuestionModal').modal('show');

          comenzarRegistroEvidencia();
        }

      }).catch(function(error) {
        console.log('Error: ' + error)
      });

    }

    async function cerrarModal() {

      if (total > 0 && haCambiadoInput == true) {

        swal({
          title: 'No ha guardado los cambios. Perdera los datos. ¿Desea continuar?',
          showDenyButton: true,
          showCancelButton: true,
          confirmButtonText: '<i class="fas fa-save"></i> Aceptar',
          confirmButtonColor: '#007bff',
          cancelButtonColor: '#6c757d',
          cancelButtonText: '<i class="fas fa-ban"></i> Cerrar',


        }).then((result) => {

          if (result) {
            //console.log("Fuera");

            haCambiadoInput = false
            closeModal();

          } else {
            //console.log("No fuera");
          }
        })


      } else {
        closeModal();
      }

    }

    async function comenzarRegistroEvidencia() {
      resetearFormulario();
      await loadQuestions({
        id: nodos_ordenados[numero_nodo_ordenado]
      });
    }

    async function siguienteRegistroEvidencia() {
      //if( !nodo_evaluado && total > 0 && haCambiadoInput == true){
      if (total > 0 && haCambiadoInput == true) {
        swal({
          title: 'No ha guardado los cambios. Perdera los datos. ¿Desea continuar?',
          showDenyButton: true,
          showCancelButton: true,
          confirmButtonText: '<i class="fas fa-save"></i> Aceptar',
          confirmButtonColor: '#007bff',
          cancelButtonColor: '#6c757d',
          cancelButtonText: '<i class="fas fa-ban"></i> Cerrar',

        }).then((result) => {
          //console.log(result);
          if (result && numero_nodo_ordenado < (nodos_ordenados.length - 1)) {
            haCambiadoInput = false;
            numero_nodo_ordenado = numero_nodo_ordenado + 1;
            comenzarRegistroEvidencia()
          }
        })
      } else if (!nodo_evaluado && total == 0) {

        swal({
          title: '¿Desea continuar sin realizar un registro?',
          showDenyButton: true,
          showCancelButton: true,
          confirmButtonText: '<i class="fas fa-save"></i> Aceptar',
          confirmButtonColor: '#007bff',
          cancelButtonColor: '#6c757d',
          cancelButtonText: '<i class="fas fa-ban"></i> Cerrar',
        }).then((result) => {
          if (result && numero_nodo_ordenado < (nodos_ordenados.length - 1)) {

            haCambiadoInput = false
            numero_nodo_ordenado = numero_nodo_ordenado + 1;
            comenzarRegistroEvidencia()
          }
        })

      } else {

        numero_nodo_ordenado = numero_nodo_ordenado + 1;
        comenzarRegistroEvidencia()
      }

    }

    async function anteriorRegistroEvidencia() {
      if (total > 0 && haCambiadoInput == true) {
        swal({
          title: 'No ha guardado los cambios. Perdera los datos. ¿Desea continuar?',
          showDenyButton: true,
          showCancelButton: true,
          confirmButtonText: '<i class="fas fa-save"></i> Aceptar',
          confirmButtonColor: '#007bff',
          cancelButtonColor: '#6c757d',
          cancelButtonText: '<i class="fas fa-ban"></i> Cerrar',
        }).then((result) => {
          if (result && numero_nodo_ordenado > 0) {
            haCambiadoInput = false;
            numero_nodo_ordenado = numero_nodo_ordenado - 1;
            comenzarRegistroEvidencia()
          }
        })
      } else if (!nodo_evaluado && total == 0) {
        swal({
          title: '¿Desea continuar sin realizar un registro?',
          showDenyButton: true,
          showCancelButton: true,
          confirmButtonText: '<i class="fas fa-save"></i> Aceptar',
          confirmButtonColor: '#007bff',
          cancelButtonColor: '#6c757d',
          cancelButtonText: '<i class="fas fa-ban"></i> Cerrar',
        }).then((result) => {
          if (result && numero_nodo_ordenado > 0) {
            haCambiadoInput = false
            numero_nodo_ordenado = numero_nodo_ordenado - 1;
            comenzarRegistroEvidencia()
          }
        })
      } else {
        numero_nodo_ordenado = numero_nodo_ordenado - 1;
        comenzarRegistroEvidencia()
      }
    }


    async function obtenerTotalTemas() {
      var total_temas = 0
      await axios({
        method: 'get',
        url: "http://67.207.86.184/obtenerTotalTemas",
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
      }).then(function(response) {
        total_temas = response.data[0][0].total;
        document.getElementById("total_nodos_por_ponderar").innerHTML = " " + total_temas;
      }).catch(function(error) {
        console.log('Error: ' + error)
      });
      return total_temas;
    }

    async function obtenerCaminos() {

      var caminos = [] //sacar el contenido que tiene el metodo axios

      //await obtiene los datos del servidor
      await axios({
        method: 'get',
        url: "http://67.207.86.184/arbol/caminos",
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
      }).then(function(response) {
        //console.log(response);

        var caminoss = response.data.caminos //respuesta de servidor
        var arreglo_nodos = [];
        var arreglo_nodos_id = [];
        //console.log(ramas);

        for (var i = 0; i < caminoss.length; i++) {
          caminoss[i] = caminoss[i].slice(1, caminoss[i].length);
        }

        var arreglo_de_arreglos = []
        for (var i = 0; i < ramas.length; i++) {
          var solo_arreglo = []
          for (var j = 0; j < caminoss.length; j++) {
            if (caminoss[j][0].id == ramas[i].id) {
              for (var k = 1; k < caminoss[j].length; k++) {
                solo_arreglo.push(caminoss[j][k]);
                //solo_arreglo.push( caminoss[i].slice(1, caminoss[i].length) );
              }
            }
          }
          arreglo_de_arreglos.push(solo_arreglo);
        }


        for (var k = 0; k < arreglo_de_arreglos.length; k++) {
          var arr = arreglo_de_arreglos[k];
          for (let i = 1; i < arr.length; i++) {
            for (let j = 0; j < arr.length - i; j++) {
              if (arr[j].nivel > arr[j + 1].nivel) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
              }
            }
          }

          for (let i = 0; i < arr.length; i++) {
            arreglo_nodos.push(arr[i].id);
          }
        }

        let uniqueArray = arreglo_nodos.filter((c, index) => {
          return arreglo_nodos.indexOf(c) === index;
        });

        //console.log("ramas");
        //console.log(ramas);
        //Quitar esto para considerar las ramas del area diciplinar
        for (var i = 0; i < ramas.length; i++) {
          for (var j = 0; j < uniqueArray.length; j++) {
            if (ramas[i].id == uniqueArray[j]) {
              uniqueArray.splice(j, 1);
              break;
            }
          }
        }

        caminos = uniqueArray;

        closeModal();


      }).catch(function(error) {
        console.log('Error: ' + error)
      });

      //console.log(caminos);

      return caminos;
    }

    async function obtenerRamas() {

      var ramas = []
      await axios({
        method: 'get',
        url: "http://67.207.86.184/arbol/obtenerRamas",
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
      }).then(function(response) {
        //console.log(response);
        ramas = response.data
      }).catch(function(error) {
        console.log('Error: ' + error)
      });
      return ramas;

    }

    async function changeParent() {
      var oldParent = document.getElementById("oldParentSelect").value;
      var newParent = document.getElementById("newParentSelect").value;
      var children = document.getElementById("childrenSelect").value;
      var color = document.getElementById("colorParentConnection").value;
      color = color.slice(1);
      actualizarPadre(oldParent, newParent, children, color);
      $('#CambiarConexionPadre').modal('hide');
      window.location.href = "http://67.207.86.184/historialexperto?x=" + x_init + "&y=" + y_init + "&e=" + e_init;
    }

    async function habilitarDesplazamiento() {
      let checkMoverNodos = document.getElementById("moverNodosCheck");
      desplazamientoDeNodos = !desplazamientoDeNodos;
    }

    async function saludarDesdeGrafoNodos(){
      console.log("Saludos desde la vista de grafo de alumnos");
    }


    async function obtenerPoderacionesNodos() 
   {

    
      var ramas = []
      await axios({
        method: 'get',
        url: "http://67.207.86.184/arbol/poderacionesNodos",
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
      }).then(function(response) {
        ramas = response.data
      }).catch(function(error) {
        console.log('Error: ' + error)
      });
      return ramas;

     // return 0;
    }

    async function obtenerRA() 
   {
      var ramas = []
      await axios({
        method: 'get',
        url: "http://67.207.86.184/arbol/obtenerRA",
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
      }).then(function(response) {
        console.log(response);
        ramas = response.data
      }).catch(function(error) {
        console.log('Error: ' + error)
      });
      return ramas;

   }