var modal_comfirm = null;
var modalMsgObj = null;
var modalBtnDelete = null;

function checkboxOnChange(obj) {
  var trObj = obj.parentElement.parentElement;
  trObj.classList.toggle("selected");
}

function getSelectedItems() {
  var checkboxes = document.getElementsByName("eventtype_ids");
  var ids = [];
  for (checkbox of checkboxes) {
    if (checkbox.checked) {
      ids.push(checkbox.value);
    }
  }
  return ids;
}

function deleteBtnOnClick() {
  if (modal_comfirm == null) {
    var divObj = document.getElementById("modal-comfirmTodelete");
    if (divObj == null) {
      return;
    }
    modal_comfirm = new bootstrap.Modal(divObj, {
      keyboard: false,
    });
    modalMsgObj = document.getElementById("modal-message");
    modalBtnDelete = document.getElementById("btn-modal-delete");
  }
  var ids = getSelectedItems();
  if (ids.length == 0) {
    modalBtnDelete.style.display = "none";
    modalMsgObj.innerText =
      "Please select at least one event type you want to delete";
  } else {
    modalBtnDelete.style.display = "block";
    modalMsgObj.innerText =
      "Are you sure delete these event types? it will delete the events which belong those event types";
  }
  modal_comfirm.show();
}

function comfirmDelBtnOnClick(params) {
  document.getElementById("itemsForm").submit();
}

function  pageOnLoad() {
   var alertNode = document.getElementById("alert-msg");
   if(alertNode!=null){
     setTimeout(() => {
        var bsalert =  new bootstrap.Alert(alertNode);
        bsalert.close();
     }, 1500);
   }
}