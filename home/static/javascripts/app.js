$(document).ready(function() {
    fixedFooter();
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
});

$(document).ready(function() {
    schedule_table.init("#reserve-table");

    $(".date-available").click(function() {
        $(".date-available").removeClass("date-selected");
        var $td = $(this);
        $td.addClass("date-selected");
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
            console.log('next');
            self.to_next_week();
        });
        self.schedule.find("#prev_week_btn").click(function() {
            console.log('prev');
            self.to_prev_week();
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
        var current_hidden_slot = self.schedule.find(".time-slot.hidden-xs")
        if (current_hidden_slot.length == 0) {
            self.schedule.find(".time-slot.week-2").addClass("hidden-xs");
        }
    },
    display_two_weeks: function() {

    },
    to_next_week: function() {
        var self = this;
        var current_hidden_slot = self.schedule.find(".time-slot.hidden-xs");
        if (current_hidden_slot.hasClass("week-2")) {
            current_hidden_slot.removeClass("hidden-xs");
            self.schedule.find(".time-slot.week-1").addClass("hidden-xs");
        }
    },
    to_prev_week: function() {
        var self = this;
        var current_hidden_slot = self.schedule.find(".time-slot.hidden-xs");
        if (current_hidden_slot.hasClass("week-1")) {
            current_hidden_slot.removeClass("hidden-xs");
            self.schedule.find(".time-slot.week-2").addClass("hidden-xs");
        }
    }
}
