function eventListMouseLeave(obj) {
  obj.style.boxShadow = "none";
}

function eventListMouseOver(obj, color) {
  obj.style.boxShadow = "0px 0px 10px " + color;
}

function detailpage(url) {
  window.location.href = url;
}

function eventNew(eventTypeCount, url) {
  if (eventTypeCount > 0) {
    window.location.href = url;
  } else {
    modal_eventTypeEmpty = new bootstrap.Modal(
      document.getElementById("modal-eventTypeEmpty"),
      {
        keyboard: false,
      }
    );
    modal_eventTypeEmpty.show();
  }
}

function pageOnLoad() {
  var alertNode = document.getElementById("alert-msg");
  if (alertNode != null) {
    setTimeout(() => {
      var bsalert = new bootstrap.Alert(alertNode);
      bsalert.close();
    }, 1500);
  }
}
