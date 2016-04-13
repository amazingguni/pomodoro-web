Deploy Provisioning NOTE
===================================

## 필요 Package

* nginx
* Python 3
* Git
* pip
* virtualenv

Ubuntu에서 실행 방법 예:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx 가상 호스트 설정

* nginx.template.conf 참고
* SITENAME 부분을 다음과 같이 수정 staging.my-domain.com

## Upstart Job

* gunicorn-upstart.template.conf 참고
* SITENAME 부분을 다음과 같이 수정 staging.my-domain.com

## 폴더 구조:
사용자 계정의 홈 폴더가 /home/username이라고 가정

/home/username
└── sites
    └── stagingserver
        ├── database
        ├── source
        ├── static
        └── virtualenv


아래 2개 파일을 SITENAME 변경 후 사용

- nginx.template.conf
    SITENAME으로 이름 변경, ln -s ~~~~로 심볼릭 깅크를 걸어 /etc/nginx/site-* 에 넣어줌

- gunicorn-upstart.tem
