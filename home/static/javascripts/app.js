
$(document).ready(function() {
  schedule_table.init("#reserve-table");
});

var schedule_table = {
  init: function(table) {
    this.schedule = $(table);
    this.event_handle();

    if ($(window).width() < 768) {
      this.small_screen_handle();
    }else{
      this.wide_screen_handle();
    }
  },
  // Execute code each time window size changes
  event_handle: function(){
    var self = this;
    // resize
    $(window).resize(function(){
      if ($(window).width() < 768) {
        self.small_screen_handle();
      }else{
        self.wide_screen_handle();
      }
    });
    // clicks
    self.schedule.find("#next_week_btn").click(function(){
      self.to_next_week($(this).data("url"));
    });
    self.schedule.find("#prev_week_btn").click(function(){
      self.to_prev_week($(this).data("url"));
    });
    // time slot click
    self.schedule.find(".date-available").click(function(){
        self.schedule.find(".date-available").removeClass("date-selected");
        var $td = $(this);
        $td.addClass("date-selected");
        window.location.href = $td.data('url');
    });
  },
  small_screen_handle: function(){
    var self = this;
    self.schedule.find(".day-title").attr("colspan", "7");
    self.schedule.find(".navigate-week-btn").addClass("small-screen");
    self.display_one_week();
  },
  wide_screen_handle: function(){
    var self = this;
    self.schedule.find(".navigate-week-btn").removeClass("small-screen");
    self.schedule.find(".day-title").attr("colspan", "14");
  },
  display_one_week: function(){
    var self = this;
    var direction= getUrlVars()["direction"];
    var current_hidden_slot = self.schedule.find(".time-slot.hidden-xs")
    if (current_hidden_slot.length == 0){
      if (direction == "prev"){
        self.schedule.find(".time-slot.week-1").addClass("hidden-xs");
      } else {
        self.schedule.find(".time-slot.week-2").addClass("hidden-xs");
      }

    }
  },
  display_two_weeks: function(){

  },
  to_next_week: function(url){
    var self = this;
    var current_hidden_slot = self.schedule.find(".time-slot.hidden-xs");
    if (current_hidden_slot.hasClass("week-2")){
      current_hidden_slot.removeClass("hidden-xs");
      self.schedule.find(".time-slot.week-1").addClass("hidden-xs");
      return;
    }
    window.location.href = url;
  },
  to_prev_week: function(url){
    var self = this;
    var current_hidden_slot = self.schedule.find(".time-slot.hidden-xs");
    if (current_hidden_slot.hasClass("week-1")){
      current_hidden_slot.removeClass("hidden-xs");
      self.schedule.find(".time-slot.week-2").addClass("hidden-xs");
      return;
    }
    window.location.href = url;
  }
}

function getUrlVars()
{
    var vars = [], hash;
    var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for(var i = 0; i < hashes.length; i++)
    {
        hash = hashes[i].split('=');
        vars.push(hash[0]);
        vars[hash[0]] = hash[1];
    }
    return vars;
}
