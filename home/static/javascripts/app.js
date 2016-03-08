
(function() {
  var autoLink,
    __slice = [].slice;

  autoLink = function() {
    var k, linkAttributes, option, options, pattern, v;
    options = 1 <= arguments.length ? __slice.call(arguments, 0) : [];

    pattern = /(^|[\s\n]|<br\/?>)((?:https?|ftp):\/\/[\-A-Z0-9+\u0026\u2019@#\/%?=()~_|!:,.;]*[\-A-Z0-9+\u0026@#\/%=~()_|])/gi;
    if (!(options.length > 0)) {
      return this.replace(pattern, "$1<a href='$2' target='_blank'>$2</a>");
    }
    option = options[0];
    linkAttributes = ((function() {
      var _results;
      _results = [];
      for (k in option) {
        v = option[k];
        if (k !== 'callback') {
          _results.push(" " + k + "='" + v + "'");
        }
      }
      return _results;
    })()).join('');
    return this.replace(pattern, function(match, space, url) {
      var link;
      link = (typeof option.callback === "function" ? option.callback(url) : void 0) || ("<a href='" + url + "'" + linkAttributes + "target='_blank'" + ">" + url + "</a>");
      return "" + space + link;
    });
  };

  String.prototype['autoLink'] = autoLink;

}).call(this);


$(document).ready(function() {
    setTimeout(function(){
      fixedFooter();
      autoLink();
    },100);

    $(window).resize(function() {
        fixedFooter();

    });

    function fixedFooter() {
        var w = window.innerHeight;
        var header = $('#header').height();
        var main = $('#main').height();
        var footer = $('#footer').height();

        if ((header + main + footer) < w) {
            $('#main').css({ minHeight: (w - header - footer - 62) + 'px' });
        }
    }

    function autoLink() {
        $('.panel-clinic-store').each(function() {
            var html = $(this).html();
            $(this).html(html.autoLink());
        })
        
    }
});

$(document).ready(function() {
    schedule_table.init("#reserve-table");

    $("#btn-submit").click(function(){
        $.LoadingOverlay("show");
    });
});

var schedule_table = {
    init: function(table) {
        this.schedule = $(table);
        this.event_handle();

        if ($(window).width() < 768) {
            this.small_screen_handle();
        } else {
            this.wide_screen_handle();
        }
    },
    // Execute code each time window size changes
    event_handle: function() {
        var self = this;
        // resize
        $(window).resize(function() {
            if ($(window).width() < 768) {
                self.small_screen_handle();
            } else {
                self.wide_screen_handle();
            }
        });
        // clicks
        self.schedule.find("#next_week_btn").click(function() {
            self.to_next_week($(this).data("url"));
        });
        self.schedule.find("#prev_week_btn").click(function() {
            self.to_prev_week($(this).data("url"));
        });
        // time slot click
        self.schedule.find(".date-available").click(function() {
            self.schedule.find(".date-available").removeClass("date-selected");
            var $td = $(this);
            if ($td.hasClass("date-available")) {
              $td.addClass("date-selected");
              $.get( $td.data("check"), function( data ) {
                if (data.status[0] == "4") {
                  $td.html("☓");
                  $td.removeClass(".date-available");
                } else if (data.status[0] == "0") {
                  window.location.href = $td.data('url') + "&token=" + data.token;
                }
              });
            }
        });
    },
    small_screen_handle: function() {
        var self = this;
        self.schedule.find(".day-title").attr("colspan", "7");
        self.schedule.find(".navigate-week-btn").addClass("small-screen");
        self.display_one_week();
    },
    wide_screen_handle: function() {
        var self = this;
        self.schedule.find(".navigate-week-btn").removeClass("small-screen");
        self.schedule.find(".day-title").attr("colspan", "14");
    },
    display_one_week: function() {
        var self = this;
        var direction = getUrlVars()["direction"];
        var current_hidden_slot = self.schedule.find(".time-slot.hidden-xs");
        if (current_hidden_slot.length == 0) {
            if (direction == "prev#schedule_subtitle") {
                self.schedule.find(".time-slot.week-1").addClass("hidden-xs");
                self.display_week_label(".week-2");
            } else {
                self.schedule.find(".time-slot.week-2").addClass("hidden-xs");
                self.display_week_label(".week-1");
            }
        }
    },
    display_week_label: function(week_displaying_selector) {
      var month_splitter = $(week_displaying_selector).find(".month-split");
      $(".month-lbl").removeClass("hidden-xs");
      if (month_splitter.length > 0) {
        $(".month-lbl.month-start, .month-lbl.month-end").addClass("hidden-xs");
      }
      else if (week_displaying_selector == ".week-1") {
        $(".month-lbl.two-months, .month-lbl.month-end").addClass("hidden-xs");
      }
      else if (week_displaying_selector == ".week-2") {
        $(".month-lbl.two-months, .month-lbl.month-start").addClass("hidden-xs");
      }
    },
    display_two_weeks: function() {

    },
    to_next_week: function(url) {
        var self = this;
        var current_hidden_slot = self.schedule.find(".time-slot.hidden-xs");
        if (current_hidden_slot.hasClass("week-2")) {
            current_hidden_slot.removeClass("hidden-xs");
            self.schedule.find(".time-slot.week-1").addClass("hidden-xs");
            self.display_week_label(".week-2");
            return;
        }
        window.location.href = url;
    },
    to_prev_week: function(url) {
        var self = this;
        var current_hidden_slot = self.schedule.find(".time-slot.hidden-xs");
        if (current_hidden_slot.hasClass("week-1")) {
            current_hidden_slot.removeClass("hidden-xs");
            self.schedule.find(".time-slot.week-2").addClass("hidden-xs");
            self.display_week_label(".week-1");
            return;
        }
        window.location.href = url;
    }
}

function getUrlVars() {
    var vars = [],
        hash;
    var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for (var i = 0; i < hashes.length; i++) {
        hash = hashes[i].split('=');
        vars.push(hash[0]);
        vars[hash[0]] = hash[1];
    }
    return vars;
}
