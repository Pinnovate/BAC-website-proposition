if [[ $UID != 0 ]]; then
    echo "Vous devez executer ce script avec la commande sudo:"
    echo "sudo $0 $*"
    exit 1
fi

current_dir=$(pwd)

wget -nc http://nginx.org/download/nginx-1.6.3.tar.gz
# wget -nc https://github.com/openresty/redis2-nginx-module/archive/v0.11.tar.gz
wget -nc http://people.freebsd.org/~osa/ngx_http_redis-0.3.7.tar.gz
wget -nc https://github.com/simpl/ngx_devel_kit/archive/v0.2.19.tar.gz
wget -nc https://github.com/openresty/set-misc-nginx-module/archive/v0.28.tar.gz

tar -xzvf nginx-1.6.3.tar.gz
# tar -xzvf v0.11.tar.gz
tar -xzvf ngx_http_redis-0.3.7.tar.gz
tar -xzvf v0.2.19.tar.gz
tar -xzvf v0.28.tar.gz

cd nginx-1.6.3
./configure --prefix=/opt/nginx \
                --add-module="$current_dir/ngx_http_redis-0.3.7" \
		--add-module="$current_dir/ngx_devel_kit-0.2.19" \
		--add-module="$current_dir/set-misc-nginx-module-0.28"
make -j2
make install
