radios
======

radios I listen


Usage
=====

basic:
`mplayer -playlist file.pls`

Fancy:

`ls **/* | dmenu | xargs mplayer -playlist`


Emacs:

```lisp

(defun radio ()
  (interactive)
  (let ((filename (ido-completing-read
                    "which radio?: "
                    (find-lisp-find-files "~/bin/radios/"
                                          (rx "." (or "pls" "asx" "m3u" "m4a") eol))
                                          nil
                                          t))
        (async-shell-command-buffer 'confirm-kill-process)
        (display-buffer-alist '(("*mplayer*" . (display-buffer-no-window)))))

    (if (s-matches-p "vlc" filename)
        (async-shell-command (concat "cvlc " filename) "*mplayer*")
      (async-shell-command (concat "mplayer -playlist " filename) "*mplayer*"))
    (with-current-buffer "*mplayer*"
      (setq show-trailing-whitespace nil))
    (message "choosen: %s" filename)))


(defun kill-radio ()
  (interactive)
  (ignore-errors
    (kill-buffer "*mplayer*")))
```
