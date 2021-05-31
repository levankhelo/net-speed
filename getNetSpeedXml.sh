#!/bin/bash

/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | grep Rate | sed 's/: / value=\"/g;s/   */    </g;s/$/\" \/>/g;1s/^/<root>\n/g;$s/$/\n<\/root>/g' > $1;