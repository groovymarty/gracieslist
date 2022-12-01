#!/bin/bash
curl -s -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0" https://www.apartments.com/wabasha-county-mn/ | \
sed -n -e '/"property-link"/p;/"property-title"/p;/"property-address"/p;/"price-range"/p;/"bed-range"/p;'
