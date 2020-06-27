import 'bootstrap';
import $ from 'jquery';
import bsCustomFileInput from 'bs-custom-file-input';

(function () {
  $(document).ready(function () {
    bsCustomFileInput.init()
    $('[data-toggle="tooltip"]').tooltip()
  });
})();
