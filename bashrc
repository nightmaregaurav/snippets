if [[ "$0" == *zsh ]]; then
  isbash="false"
  iszsh="true"
else
  isbash="true"
  iszsh="false"
fi;

# If not running interactively, don't do anything
case $- in
  *i*);;
  *) return;;
esac

# If started from sshd, make sure profile is sourced
if [[ -n "$SSH_CONNECTION" ]] && [[ "$PATH" != *:/usr/bin* ]]; then
  . /etc/profile
fi

# Source global definitions
if [[ $isbash == "true" ]]; then
  if [ -f /etc/bashrc ]; then
    . /etc/bashrc
  fi
fi
if [[ $iszsh == "true" ]]; then
  if [ -f /etc/zshrc ]; then
    . /etc/zshrc
  fi
fi

# Don't put duplicate lines in the history and do not add lines that start with a space
export HISTCONTROL=erasedups:ignoredups:ignorespace

# Causes bash to append to history instead of overwriting it so if you start a new terminal, you have old session history
[[ $isbash == "true" ]] && shopt -s histappend
PROMPT_COMMAND='history -a'

# Don't consider certain characters part of the word
WORDCHARS=${WORDCHARS//\/}

# hide EOL sign ('%')
PROMPT_EOL_MARK=""

# Expand the history size
export HISTFILESIZE=10000
export HISTSIZE=2000

# Check the window size after each command and, if necessary, update the values of LINES and COLUMNS
[[ $isbash == "true" ]] && shopt -s checkwinsize

# Makes less more friendly for non-text input files
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# Allow ctrl-S for history navigation (with ctrl-R)
stty -ixon

# Ignore case on auto-completion
# Note: bind used instead of sticking these in .inputrc
if [[ $iatest > 0 ]]; then bind "set completion-ignore-case on"; fi

# Show auto-completion list automatically, without double tab
if [[ $iatest > 0 ]]; then bind "set show-all-if-ambiguous On"; fi

# To have colors for ls and all grep commands such as grep, egrep and zgrep
export CLICOLOR=1
export LS_COLORS='no=00:fi=00:di=00;34:ln=01;36:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:ex=01;32:ow=30;44:*.tar=01;31:*.tgz=01;31:*.arj=01;31:*.taz=01;31:*.lzh=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.gz=01;31:*.bz2=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.avi=01;35:*.fli=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.ogg=01;35:*.mp3=01;35:*.wav=01;35:*.xml=00;31:'
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
alias zgrep='zgrep --color=auto'
alias diff='diff --color=auto'
alias ip='ip --color=auto'

# colored GCC warnings and errors
export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# Color for manpages in less makes manpages a little easier to read
export LESS_TERMCAP_mb=$'\E[1;31m'     # begin blink
export LESS_TERMCAP_md=$'\E[1;36m'     # begin bold
export LESS_TERMCAP_me=$'\E[0m'        # reset bold/blink
export LESS_TERMCAP_so=$'\E[01;33m'    # begin reverse video
export LESS_TERMCAP_se=$'\E[0m'        # reset reverse video
export LESS_TERMCAP_us=$'\E[1;32m'     # begin underline
export LESS_TERMCAP_ue=$'\E[0m'        # reset underline

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Force to show the complete history
alias history="history 0"

# Add an "alert" alias for long running commands.  Use like: sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Edit this .bashrc file
alias ebrc='edit ~/.bashrc'

# alias to show the date
alias da='date "+%Y-%m-%d %A %T %Z"'

# Show open ports
alias openports='netstat -nape --inet'

# Get public IP address
alias publicip='curl -s ipinfo.io/ip'

# Get CPU usage
alias cpu="grep 'cpu ' /proc/stat | awk '{usage=(\$2+\$4)*100/(\$2+\$4+\$5)} END {print usage}' | awk '{printf(\"%.1f\n\", \$1)}'"

# Alias's for archives
alias mktar='tar -cvf'
alias mkbz2='tar -cvjf'
alias mkgz='tar -cvzf'
alias untar='tar -xvf'
alias unbz2='tar -xvjf'
alias ungz='tar -xvzf'

# Alias's to modified commands
alias cp='cp -i'
alias mv='mv -i'
alias rm='rm -iv'
alias mkdir='mkdir -p'
alias ps='ps auxf'
alias ping='ping -c 10'
alias less='less -R'
alias cls='clear'

# Change directory aliases
alias home='cd ~'
alias cd..='cd ..'
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias .....='cd ../../../..'

# alias chmod commands
alias 000='chmod -R 000'
alias 644='chmod -R 644'
alias 666='chmod -R 666'
alias 755='chmod -R 755'
alias 744='chmod -R 744'
alias 774='chmod -R 774'
alias 777='chmod -R 777'

# Configure `time` format
TIMEFMT=$'\nreal\t%E\nuser\t%U\nsys\t%S\ncpu\t%P'

# Source bashalias if available
if [ -f ~/.bash_aliases ]; then
  . ~/.bash_aliases
fi

# Get free port after a port
function freeportafter
{
  blank=$(echo " " | tr -d ' ' | tr -d '  ' | tr -d '\n');
  port=$*;

  if [[ "$port" == "$blank" ]]; then
    port=5000;
  fi;

  myarray=($(lsof -i -P -n | grep LISTEN | awk '{print $9}' | awk -F: '{print $NF}' | awk '$1 >= '"$port"' {print $1}' | sort -un));

  for i in "${myarray[@]}"
  do
    if [[ $i == $port ]]; then
      port=$((port+1));
    else
      break;
    fi;
  done;

  echo $port;
}


#######################################################
#          Set the amazing command prompt             #
#######################################################
function __setprompt
{
  local LAST_COMMAND=$? # Must come first!
  local NEWLINE=$'\n'

  PS1=""
  PS2=""
  PS3=""
  PS4=""

  # Define colors and other variables
  if [[ $isbash == "true" ]]; then
    local RED="\[\033[0;31m\]"
    local GREEN="\[\033[0;32m\]"
    local YELLOW="\[\033[0;33m\]"
    local BLUE="\[\033[0;34m\]"
    local MAGENTA="\[\033[0;35m\]"
    local CYAN="\[\033[0;36m\]"
    local NOCOLOR="\[\033[0m\]"
    local BOLD="\[\033[1m\]"

    local PERCENTAGE="%"
    local HOSTNAME="\h"
    local CWD="\w"
    local USERNAME="\u"
  fi
  if [[ $iszsh == "true" ]]; then
    local RED="%F{red}"
    local GREEN="%F{green}"
    local YELLOW="%F{yellow}"
    local BLUE="%F{blue}"
    local MAGENTA="%F{magenta}"
    local CYAN="%F{cyan}"
    local NOCOLOR="%b%f%F{reset}"
    local BOLD="%B"

    local PERCENTAGE="%%"
    local HOSTNAME="%M"
    local CWD="%~"
    local USERNAME="%n"
  fi

  # set color only when we know we can use color
  if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
    local color_prompt=yes
  else
    local color_prompt=
  fi

  # unset color and style codes if we don't want colors
  if ! [ "$color_prompt" = yes ]; then
    local RED=""
    local GREEN=""
    local YELLOW=""
    local BLUE=""
    local MAGENTA=""
    local CYAN=""
    local NOCOLOR=""
    local BOLD=""
  fi

  # Show error exit code if there is one
  if [[ $LAST_COMMAND != 0 ]]; then
    PS1+="${NOCOLOR}(${RED}${BOLD}ERROR${NOCOLOR})-(${RED}${BOLD}Exit Code ${NOCOLOR}${LAST_COMMAND}${NOCOLOR})-(${RED}${BOLD}"
    if [[ $LAST_COMMAND == 1 ]]; then
      PS1+="General error"
    elif [ $LAST_COMMAND == 2 ]; then
      PS1+="Missing keyword, command, or permission problem"
    elif [ $LAST_COMMAND == 126 ]; then
      PS1+="Permission problem or command is not an executable"
    elif [ $LAST_COMMAND == 127 ]; then
      PS1+="Command not found"
    elif [ $LAST_COMMAND == 128 ]; then
      PS1+="Invalid argument to exit"
    elif [ $LAST_COMMAND == 129 ]; then
      PS1+="Fatal error signal 1"
    elif [ $LAST_COMMAND == 130 ]; then
      PS1+="Script terminated by Control-C"
    elif [ $LAST_COMMAND == 131 ]; then
      PS1+="Fatal error signal 3"
    elif [ $LAST_COMMAND == 132 ]; then
      PS1+="Fatal error signal 4"
    elif [ $LAST_COMMAND == 133 ]; then
      PS1+="Fatal error signal 5"
    elif [ $LAST_COMMAND == 134 ]; then
      PS1+="Fatal error signal 6"
    elif [ $LAST_COMMAND == 135 ]; then
      PS1+="Fatal error signal 7"
    elif [ $LAST_COMMAND == 136 ]; then
      PS1+="Fatal error signal 8"
    elif [ $LAST_COMMAND == 137 ]; then
      PS1+="Fatal error signal 9"
    elif [ $LAST_COMMAND -gt 255 ]; then
      PS1+="Exit status out of range"
    else
      PS1+="Unknown error code"
    fi
    PS1+=")${NOCOLOR}${NEWLINE}"
  else
    PS1+=""
  fi

  # Date
  PS1+="${NOCOLOR}(${CYAN}${BOLD}$(date +%a) $(date +%b-'%-m')" # Date
  PS1+="${BLUE}${BOLD} $(date +'%-I':%M%P)${NOCOLOR})-" # Time

  # CPU
  PS1+="(${MAGENTA}${BOLD}CPU $(cpu)${PERCENTAGE}${NOCOLOR})-"

  # hostname
  PS1+="(${YELLOW}${BOLD}${HOSTNAME}"

  # Current directory
  PS1+="${NOCOLOR}:${YELLOW}${CWD}${NOCOLOR})"

  # Current Global IP
  IP=$(publicip)
  if [[ "$IP" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    PS1+="-(${RED}${BOLD}${IP}${NOCOLOR})"
  fi

  # Skip to the next line
  PS1+="${NEWLINE}"

  if [[ $EUID -ne 0 ]]; then
    PS1+="${NOCOLOR}(${GREEN}${BOLD}${USERNAME}${NOCOLOR}) ${YELLOW}${BOLD}$(git rev-parse --abbrev-ref HEAD 2> /dev/null)${NOCOLOR}${GREEN} >>>${NOCOLOR} " # Normal user
  else
    PS1+="${NOCOLOR}(${RED}${BOLD}${USERNAME}${NOCOLOR}) ${YELLOW}${BOLD}$(git rev-parse --abbrev-ref HEAD 2> /dev/null)${NOCOLOR}${RED} >>>${NOCOLOR} " # Root user
  fi

  # Add python virtual env name if available
  if [ -z "${VIRTUAL_ENV_DISABLE_PROMPT}" ] ; then
    env_name=$(basename "$VIRTUAL_ENV")
    if ! [ -z "${env_name}" ] ; then
      PS1="[${env_name}]-${PS1}"
    fi
  fi

  # PS2 is used to continue a command using the \ character

  PS2+="${GREEN} >>>${NOCOLOR} "

  # PS3 is used to enter a number choice in a script
  PS3+="${GREEN} Enter a number from the list above:${NOCOLOR} "

  # PS4 is used for tracing a script in debug mode
  PS4+="${GREEN}+${NOCOLOR} "
}

# Enable bash programmable completion features in interactive shells
if [[ $isbash == "true" ]]; then
  if ! shopt -oq posix; then
    if [ -f /usr/share/bash-completion/bash_completion ]; then
      . /usr/share/bash-completion/bash_completion
    elif [ -f /etc/bash_completion ]; then
      . /etc/bash_completion
    fi
  fi
fi

# zsh specific
if [[ $iszsh == "true" ]]; then
  setopt hist_append
  setopt hist_expire_dups_first # delete duplicates first when HISTFILE size exceeds HISTSIZE
  setopt hist_ignore_dups       # ignore duplicated commands history list
  setopt hist_ignore_space      # ignore commands that start with space
  setopt hist_verify            # show command with history expansion to user before running it
  setopt autocd                 # change directory just by typing its name
  #setopt correct               # auto correct mistakes
  setopt interactivecomments    # allow comments in interactive mode
  setopt magicequalsubst        # enable filename expansion for arguments of the form ‘anything=expression’
  setopt nonomatch              # hide error message if there is no match for the pattern
  setopt notify                 # report the status of background jobs immediately
  setopt numericglobsort        # sort filenames numerically when it makes sense
  setopt promptsubst            # enable command substitution in prompt

  # Enable completion features
  autoload -Uz compinit
  compinit -d ~/.cache/zcompdump
  zstyle ':completion:*:*:*:*:*' menu select
  zstyle ':completion:*' auto-description 'specify: %d'
  zstyle ':completion:*' completer _expand _complete
  zstyle ':completion:*' format 'Completing %d'
  zstyle ':completion:*' group-name ''
  zstyle ':completion:*' list-colors ''
  zstyle ':completion:*' list-prompt %SAt %p: Hit TAB for more, or the character to insert%s
  zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}'
  zstyle ':completion:*' rehash true
  zstyle ':completion:*' select-prompt %SScrolling active: current selection at %p%s
  zstyle ':completion:*' use-compctl false
  zstyle ':completion:*' verbose true
  zstyle ':completion:*:kill:*' command 'ps -u $USER -o pid,%cpu,tty,cputime,cmd'

  # Configure key keybindings
  bindkey -e                                        # emacs key bindings
  bindkey ' ' magic-space                           # do history expansion on space
  bindkey '^U' backward-kill-line                   # ctrl + U
  bindkey '^[[3;5~' kill-word                       # ctrl + Supr
  bindkey '^[[3~' delete-char                       # delete
  bindkey '^[[1;5C' forward-word                    # ctrl + ->
  bindkey '^[[1;5D' backward-word                   # ctrl + <-
  bindkey '^[[5~' beginning-of-buffer-or-history    # page up
  bindkey '^[[6~' end-of-buffer-or-history          # page down
  bindkey '^[[H' beginning-of-line                  # home
  bindkey '^[[F' end-of-line                        # end
  bindkey '^[[Z' undo                               # shift + tab undo last action

  # styles
  zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"
  zstyle ':completion:*:*:kill:*:processes' list-colors '=(#b) #([0-9]#)*=0=01;31'

  # Enable syntax-highlighting
  if [ -f /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh ]; then
    . /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
    ZSH_HIGHLIGHT_HIGHLIGHTERS=(main brackets pattern)
    ZSH_HIGHLIGHT_STYLES[default]=none
    ZSH_HIGHLIGHT_STYLES[unknown-token]=fg=white,underline
    ZSH_HIGHLIGHT_STYLES[reserved-word]=fg=cyan,bold
    ZSH_HIGHLIGHT_STYLES[suffix-alias]=fg=green,underline
    ZSH_HIGHLIGHT_STYLES[global-alias]=fg=green,bold
    ZSH_HIGHLIGHT_STYLES[precommand]=fg=green,underline
    ZSH_HIGHLIGHT_STYLES[commandseparator]=fg=blue,bold
    ZSH_HIGHLIGHT_STYLES[autodirectory]=fg=green,underline
    ZSH_HIGHLIGHT_STYLES[path]=bold
    ZSH_HIGHLIGHT_STYLES[path_pathseparator]=
    ZSH_HIGHLIGHT_STYLES[path_prefix_pathseparator]=
    ZSH_HIGHLIGHT_STYLES[globbing]=fg=blue,bold
    ZSH_HIGHLIGHT_STYLES[history-expansion]=fg=blue,bold
    ZSH_HIGHLIGHT_STYLES[command-substitution]=none
    ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter]=fg=magenta,bold
    ZSH_HIGHLIGHT_STYLES[process-substitution]=none
    ZSH_HIGHLIGHT_STYLES[process-substitution-delimiter]=fg=magenta,bold
    ZSH_HIGHLIGHT_STYLES[single-hyphen-option]=fg=green
    ZSH_HIGHLIGHT_STYLES[double-hyphen-option]=fg=green
    ZSH_HIGHLIGHT_STYLES[back-quoted-argument]=none
    ZSH_HIGHLIGHT_STYLES[back-quoted-argument-delimiter]=fg=blue,bold
    ZSH_HIGHLIGHT_STYLES[single-quoted-argument]=fg=yellow
    ZSH_HIGHLIGHT_STYLES[double-quoted-argument]=fg=yellow
    ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument]=fg=yellow
    ZSH_HIGHLIGHT_STYLES[rc-quote]=fg=magenta
    ZSH_HIGHLIGHT_STYLES[dollar-double-quoted-argument]=fg=magenta,bold
    ZSH_HIGHLIGHT_STYLES[back-double-quoted-argument]=fg=magenta,bold
    ZSH_HIGHLIGHT_STYLES[back-dollar-quoted-argument]=fg=magenta,bold
    ZSH_HIGHLIGHT_STYLES[assign]=none
    ZSH_HIGHLIGHT_STYLES[redirection]=fg=blue,bold
    ZSH_HIGHLIGHT_STYLES[comment]=fg=black,bold
    ZSH_HIGHLIGHT_STYLES[named-fd]=none
    ZSH_HIGHLIGHT_STYLES[numeric-fd]=none
    ZSH_HIGHLIGHT_STYLES[arg0]=fg=cyan
    ZSH_HIGHLIGHT_STYLES[bracket-error]=fg=red,bold
    ZSH_HIGHLIGHT_STYLES[bracket-level-1]=fg=blue,bold
    ZSH_HIGHLIGHT_STYLES[bracket-level-2]=fg=green,bold
    ZSH_HIGHLIGHT_STYLES[bracket-level-3]=fg=magenta,bold
    ZSH_HIGHLIGHT_STYLES[bracket-level-4]=fg=yellow,bold
    ZSH_HIGHLIGHT_STYLES[bracket-level-5]=fg=cyan,bold
    ZSH_HIGHLIGHT_STYLES[cursor-matchingbracket]=standout
  fi

  # Enable auto-suggestions based on the history
  if [ -f /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh ]; then
    . /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh
    ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=#999'
  fi

  # Enable command-not-found if installed
  if [ -f /etc/zsh_command_not_found ]; then
    . /etc/zsh_command_not_found
  fi
fi

PROMPT_COMMAND='__setprompt'
precmd_functions=(__setprompt)
