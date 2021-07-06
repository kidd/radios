radios
======

radios I listen


Usage
=====

basic:
`mplayer -playlist file.pls`

Fancy:

`ls **/* | dmenu | xargs mplayer -playlist`

Update songs
============

Update soma.fm urls via https://github.com/kidd/radios/pull/3 or
https://somafm.com/channels.json

Emacs:

```lisp

(defvar radio-list nil)
(defun radio ()
  (interactive)
  (let ((filename
         (ido-completing-read
          "which radio?: "
				  (find-lisp-find-files "~/bin/radios/"
                                (rx "." (or "pls" "asx" "m3u" "m4a") eol))
          nil
          t nil 'radio-list (first radio-list)))
        (async-shell-command-buffer 'confirm-kill-process)
        (display-buffer-alist '(("*mplayer*" . (display-buffer-no-window)))))

    (if (s-matches-p "vlc" filename)
        (async-shell-command (concat "cvlc " filename) "*mplayer*")
      (async-shell-command (concat "mplayer -playlist " filename) "*mplayer*"))
    (with-current-buffer "*mplayer*"
      (setq show-trailing-whitespace nil)
      (setq-local undo-outer-limit 100))
    (message "choosen: %s" filename)))

(setq warning-suppress-types (list '(undo discard-info)))


(defun kill-radio ()
  (interactive)
  (ignore-errors
    (kill-buffer "*mplayer*")))


(defun kill-current-song ()
  "save current song in file ~/org/music.org."
  ;; lines look like:
  ;; ICY Info: StreamTitle='radiOzora - We are all connected';
  (interactive)
  (save-excursion
    (with-current-buffer "*mplayer*"
     (end-of-buffer)
     (search-backward "ICY Info: StreamTitle='")
     (search-forward "StreamTitle='")
     (set-mark (point))
     (end-of-line)
     (search-backward "'")
     ;; (backward-char)
     (kill-region (mark) (point))
     (yank))
   (with-current-buffer (find-file-noselect "~/org/music.org")
     (end-of-buffer)
     (insert "\n* ")
     (yank)
     (insert (format "\n\n  [%s]" (format-time-string "%Y-%m-%d"))))))

(fset 'hit 'kill-current-song)
```

See also
========

If you want a fancier interface for emacs but only with soma.fm
support, check this out: https://github.com/artenator/somafm.el

Check this out: https://github.com/altdesktop/playerctl , This allows you to
manipulate your player from the commmand line, no matter if you're playing
youtube,spotify,...  Looks super!

Want more?
==========

https://news.ycombinator.com/item?id=27737887 Has lots of links you can go
explore, like:
https://open.spotify.com/user/mynameislinea/playlist/5Fq64a52kow0iivojKlad0?si=UMt5KU9LTk-myJ6Bj-GeWQ&dl_branch=1,
which is a 800h playlist with ambient music.

