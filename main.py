from flask import Flask, render_template, url_for, session, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

COMPANIES = [
    {
        'index': '0',
        'in_need': True,
        'username': 'aaa',
        'name': 'John Doe',
        'email': 'me@example.com',
        'phone': '555-555-5555',
        'password': 'aaa',
        'business_name': "For Goodness Bake ",
        'business_website': 'http://www.cnn.com',
        'business_image': '/static/biz88.jpg',
        'business_images': ['/static/biz88.jpg', '/static/cake1.jpg', '/static/cake7.jpg'],
        'business_email': 'me@example.com',
        'business_phone': '555-555-5555',
        'business_address': {
            'line1': '2601 Gentilly Blvd.',
            'line2': 'PSB 288',
            'city': 'New Orleans',
            'state': 'LA',
            'zip': '70122',
        },
        'business_description': "For Goodness Bake is your one stop shop for all types of pastries. We Bake fresh caes, bread, spring rolls, meat pis and all other delicious snacks. We at For Goodness Bake believe in the simple pleasure of a truly homemade treat. With freshness and favor at the forefront, we combine classic and contemporary ingredients to create items that pyt tist on the traditional.",
        'customers': [
            {
                'index': '0',
                'name': 'M. Elie',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '1',
                'name': 'Dr. Mustapha',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '2',
                'name': 'J. McAdams',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
        ],

    },
    {
        'index': '1',
        'in_need': True,
        'username': 'bbb',
        'name': 'John Doe',
        'email': 'me@example.com',
        'phone': '555-555-5555',
        'password': 'bbb',
        'business_name': "Hazel & Fay Cakes",
        'business_website': 'http://www.cnn.com',
        'business_image': '/static/biz99.jpg',
        'business_images': ['/static/biz99.jpg', '/static/cake2.jpg', '/static/cake3.jpg'],
        'business_email': 'me@example.com',
        'business_phone': '555-555-5555',
        'business_address': {
            'line1': '2601 Gentilly Blvd.',
            'line2': 'PSB 288',
            'city': 'New Orleans',
            'state': 'LA',
            'zip': '70122',
        },
        'business_description': "With a specialty in wedding and birthday cakes, Hazel & Fay Cakes brings to you an exceptional catering service at a low cost. We also offer delivery services to your home and provide you with discounts on your next purchase. We value our customers and provide highly customizable cakes. We also cater for large events and conferences and are very effective and efficient",
        'customers': [
            {
                'index': '0',
                'name': 'M. Elie',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '1',
                'name': 'Dr. Mustapha',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '2',
                'name': 'J. McAdams',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
        ],

    },
    {
        'index': '2',
        'in_need': True,
        'username': 'ccc',
        'name': 'John Doe',
        'email': 'me@example.com',
        'phone': '555-555-5555',
        'password': 'ccc',
        'business_name': "The village Vet",
        'business_website': 'http://www.cnn.com',
        'business_image': '/static/biz101.png',
        'business_images': ['/static/biz101.png', '/static/vet1.jpg', '/static/vet2.jpg'],
        'business_email': 'me@example.com',
        'business_phone': '555-555-5555',
        'business_address': {
            'line1': '2601 Gentilly Blvd.',
            'line2': 'PSB 288',
            'city': 'New Orleans',
            'state': 'LA',
            'zip': '70122',
        },
        'business_description': "Our unique love and care for the health and wellness of all animals makes Village Vets a great organization. We pride ourselves on being a full-service hospital, capable of handling most medical and surgical problems.  We provide a wide range of services such as preventative health care, dental care, surgery, boarding and grooming.  Our hospital staff consists of well-trained and highly qualified personnel, who constantly strive to provide the best medical and surgical care possible for our patients.   We are proud to have recently been voted as metro-Atlanta's "'Best Vets'" in the November 2012 edition of Atlanta magazine's "'Best of Atlanta'" contest - our fifth consecutive honor in this publication.",
        'customers': [
            {
                'index': '0',
                'name': 'M. Elie',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '1',
                'name': 'Dr. Mustapha',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '2',
                'name': 'J. McAdams',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
        ],

    },
    {
        'index': '3',
        'in_need': True,
        'username': 'ddd',
        'name': 'John Doe',
        'email': 'me@example.com',
        'phone': '555-555-5555',
        'password': 'ddd',
        'business_name': "The Hair & Scalp Clinic",
        'business_website': 'http://www.cnn.com',
        'business_image': '/static/biz55.jpg',
        'business_images': ['/static/biz55.jpg', '/static/hair1.jpg', '/static/hair2.jpg'],
        'business_email': 'me@example.com',
        'business_phone': '555-555-5555',
        'business_address': {
            'line1': '2601 Gentilly Blvd.',
            'line2': 'PSB 288',
            'city': 'New Orleans',
            'state': 'LA',
            'zip': '70122',
        },
        'business_description': "The Hair & Scalp Clinic is focused on providing enabling patients maintain healthy scalps and revitalized hair. We utilize a comprehensive and state of the art techniques, a successful treatment plan will be molded for each patient. Our customized efforts makes our patients choose us over our competitors which is our competitive advantage.",
        'customers': [
            {
                'index': '0',
                'name': 'M. Elie',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '1',
                'name': 'Dr. Mustapha',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '2',
                'name': 'J. McAdams',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
        ],

    },
    {
        'index': '4',
        'in_need': True,
        'username': 'eee',
        'name': 'John Doe',
        'email': 'me@example.com',
        'phone': '555-555-5555',
        'password': 'eee',
        'business_name': "Morgan Electric",
        'business_website': 'http://www.cnn.com',
        'business_image': '/static/biz44.jpg',
        'business_images': ['/static/biz44.jpg', '/static/biz44.jpg', '/static/biz44.jpg'],
        'business_email': 'me@example.com',
        'business_phone': '555-555-5555',
        'business_address': {
            'line1': '2601 Gentilly Blvd.',
            'line2': 'PSB 288',
            'city': 'New Orleans',
            'state': 'LA',
            'zip': '70122',
        },
        'business_description': "Morgan Electric is focused on delivering electrical engineering services and ensuring families and organizations have adequate electricity. We have highly qualified electricians and electrical engineers who have adequate knowledge and skills.",
        'customers': [
            {
                'index': '0',
                'name': 'M. Elie',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '1',
                'name': 'Dr. Mustapha',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '2',
                'name': 'J. McAdams',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
        ],
    },
    {
        'index': '5',
        'in_need': True,
        'username': 'fff',
        'name': 'John Doe',
        'email': 'me@example.com',
        'phone': '555-555-5555',
        'password': 'fff',
        'business_name': "Sewing Beauty Company",
        'business_website': 'http://www.cnn.com',
        'business_image': '/static/biz103.jpg',
        'business_images': ['/static/biz103.jpg', '/static/sewing1.jpg', '/static/sewing2.jpg'],
        'business_email': 'me@example.com',
        'business_phone': '555-555-5555',
        'business_address': {
            'line1': '2601 Gentilly Blvd.',
            'line2': 'PSB 288',
            'city': 'New Orleans',
            'state': 'LA',
            'zip': '70122',
        },
        'business_description': "Sewing Beauty Company is a fashion designing company known for authentic designs and materials. We sew for top celebrities in the city and attain referrals regularly because of our unique styles and the authenticity and trendiness of our styles.",
        'customers': [
            {
                'index': '0',
                'name': 'M. Elie',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '1',
                'name': 'Dr. Mustapha',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '2',
                'name': 'J. McAdams',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
        ],

    },
    {
        'index': '6',
        'in_need': True,
        'username': 'ggg',
        'name': 'John Doe',
        'email': 'me@example.com',
        'phone': '555-555-5555',
        'password': 'ggg',
        'business_name': "Roberts Tractor Repair & Sales",
        'business_website': 'http://www.cnn.com',
        'business_image': '/static/biz102.jpg',
        'business_images': ['/static/biz102.jpg', '/static/cake1.jpg', '/static/cake1.jpg'],
        'business_email': 'me@example.com',
        'business_phone': '555-555-5555',
        'business_address': {
            'line1': '2601 Gentilly Blvd.',
            'line2': 'PSB 288',
            'city': 'New Orleans',
            'state': 'LA',
            'zip': '70122',
        },
        'business_description': "We repair tractors and also sell efficient and effective tractors. Our prices are the best an we provide warranty and guarantee for all our products. We provide the best products in the tractor markets and also repair tractors.",
        'customers': [
            {
                'index': '0',
                'name': 'M. Elie',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '1',
                'name': 'Dr. Mustapha',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '2',
                'name': 'J. McAdams',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
        ],

    },
    {
        'index': '7',
        'in_need': True,
        'username': 'hhh',
        'name': 'John Doe',
        'email': 'me@example.com',
        'phone': '555-555-5555',
        'password': 'hhh',
        'business_name': "Italia House",
        'business_website': 'http://www.cnn.com',
        'business_image': '/static/biz33.jpg',
        'business_images': ['/static/biz33.jpg', '/static/cake1.jpg', '/static/cake1.jpg'],
        'business_email': 'me@example.com',
        'business_phone': '555-555-5555',
        'business_address': {
            'line1': '2601 Gentilly Blvd.',
            'line2': 'PSB 288',
            'city': 'New Orleans',
            'state': 'LA',
            'zip': '70122',
        },
        'business_description': "The Italia House is an Italian restaurant focused on providing delicious delicacies to customers. Authentic Italian meals is what Italia House is known for and our process are high affordable. We operate 24 hours every day and known for the delivery of top notch customer service.",
        'customers': [
            {
                'index': '0',
                'name': 'M. Elie',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '1',
                'name': 'Dr. Mustapha',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '2',
                'name': 'J. McAdams',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
        ],

    },
    {
        'index': '8',
        'in_need': True,
        'username': 'iii',
        'name': 'John Doe',
        'email': 'me@example.com',
        'phone': '555-555-5555',
        'password': 'iii',
        'business_name': "String Theory Yarn Company",
        'business_website': 'http://www.cnn.com',
        'business_image': '/static/biz104.gif',
        'business_images': ['/static/biz104.gif', '/static/cake1.jpg', '/static/cake1.jpg'],
        'business_email': 'me@example.com',
        'business_phone': '555-555-5555',
        'business_address': {
            'line1': '2601 Gentilly Blvd.',
            'line2': 'PSB 288',
            'city': 'New Orleans',
            'state': 'LA',
            'zip': '70122',
        },
        'business_description': "String for yarn produces yarn and also creates several products through the use of yarn. Some of our major products includes bags, sweaters, pillows, stockings and many more. Our products have high quality and will last very long. We believe in utilizing quality materials in production which is why our customers keep coming back to us.",
        'customers': [
            {
                'index': '0',
                'name': 'M. Elie',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '1',
                'name': 'Dr. Mustapha',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '2',
                'name': 'J. McAdams',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
        ],

    },
    {
        'index': '9',
        'in_need': True,
        'username': 'jjj',
        'name': 'John Doe',
        'email': 'me@example.com',
        'phone': '555-555-5555',
        'password': 'jjj',
        'business_name': "Josh's Natureville",
        'business_website': 'http://www.cnn.com',
        'business_image': '/static/biz66.jpg',
        'business_images': ['/static/biz66.jpg', '/static/cake1.jpg', '/static/cake1.jpg'],
        'business_email': 'me@example.com',
        'business_phone': '555-555-5555',
        'business_address': {
            'line1': '2601 Gentilly Blvd.',
            'line2': 'PSB 288',
            'city': 'New Orleans',
            'state': 'LA',
            'zip': '70122',
        },
        'business_description': "Lorem ipsum dolor sit amet, pro in iusto dolorum. Dicit cetero equidem vix ut, eu sed tale iisque vulputate, sea ex integre quaeque. No quaestio antiopam has. Eu alterum maiestatis pro. Id option recusabo constituto cum, vim harum tantas sadipscing ut, cum te nibh porro commodo.",
        'customers': [
            {
                'index': '0',
                'name': 'M. Elie',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '1',
                'name': 'Dr. Mustapha',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '2',
                'name': 'J. McAdams',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
        ],
    },
    {
        'index': '10',
        'in_need': True,
        'username': 'kkk',
        'name': 'John Doe',
        'email': 'me@example.com',
        'phone': '555-555-5555',
        'password': 'kkk',
        'business_name': "Kailyn's Kickers",
        'business_website': 'http://www.cnn.com',
        'business_image': '/static/biz101.png',
        'business_images': ['/static/biz101.png', '/static/cake1.jpg', '/static/cake1.jpg'],
        'business_email': 'me@example.com',
        'business_phone': '555-555-5555',
        'business_address': {
            'line1': '2601 Gentilly Blvd.',
            'line2': 'PSB 288',
            'city': 'New Orleans',
            'state': 'LA',
            'zip': '70122',
        },
        'business_description': "Lorem ipsum dolor sit amet, pro in iusto dolorum. Dicit cetero equidem vix ut, eu sed tale iisque vulputate, sea ex integre quaeque. No quaestio antiopam has. Eu alterum maiestatis pro. Id option recusabo constituto cum, vim harum tantas sadipscing ut, cum te nibh porro commodo.",
        'customers': [
            {
                'index': '0',
                'name': 'M. Elie',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '1',
                'name': 'Dr. Mustapha',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '2',
                'name': 'J. McAdams',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
        ],
    },
    {
        'index': '11',
        'in_need': True,
        'username': 'lll',
        'name': 'John Doe',
        'email': 'me@example.com',
        'phone': '555-555-5555',
        'password': 'lll',
        'business_name': "Liam's Techworld",
        'business_website': 'http://www.cnn.com',
        'business_image': '/static/biz105.jpg',
        'business_images': ['/static/biz105.jpg', '/static/cake1.jpg', '/static/cake1.jpg'],
        'business_email': 'me@example.com',
        'business_phone': '555-555-5555',
        'business_address': {
            'line1': '2601 Gentilly Blvd.',
            'line2': 'PSB 288',
            'city': 'New Orleans',
            'state': 'LA',
            'zip': '70122',
        },
        'business_description': "Lorem ipsum dolor sit amet, pro in iusto dolorum. Dicit cetero equidem vix ut, eu sed tale iisque vulputate, sea ex integre quaeque. No quaestio antiopam has. Eu alterum maiestatis pro. Id option recusabo constituto cum, vim harum tantas sadipscing ut, cum te nibh porro commodo.",
        'customers': [
            {
                'index': '0',
                'name': 'M. Elie',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '1',
                'name': 'Dr. Mustapha',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '2',
                'name': 'J. McAdams',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
        ],

    },
    {
        'index': '12',
        'in_need': True,
        'username': 'mmm',
        'name': 'John Doe',
        'email': 'me@example.com',
        'phone': '555-555-5555',
        'password': 'mmm',
        'business_name': "Mike's Tire Shop",
        'business_website': 'http://www.cnn.com',
        'business_image': '/static/biz106.png',
        'business_images': ['/static/biz106.png', '/static/cake1.jpg', '/static/cake1.jpg'],
        'business_email': 'me@example.com',
        'business_phone': '555-555-5555',
        'business_address': {
            'line1': '2601 Gentilly Blvd.',
            'line2': 'PSB 288',
            'city': 'New Orleans',
            'state': 'LA',
            'zip': '70122',
        },
        'business_description': "Lorem ipsum dolor sit amet, pro in iusto dolorum. Dicit cetero equidem vix ut, eu sed tale iisque vulputate, sea ex integre quaeque. No quaestio antiopam has. Eu alterum maiestatis pro. Id option recusabo constituto cum, vim harum tantas sadipscing ut, cum te nibh porro commodo.",
        'customers': [
            {
                'index': '0',
                'name': 'M. Elie',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '1',
                'name': 'Dr. Mustapha',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
            {
                'index': '2',
                'name': 'J. McAdams',
                'phone': '555-555-5555',
                'email': 'me@example.com',
                'address': {
                    'line1': '2601 Gentilly Blvd.',
                    'line2': 'PSB 288',
                    'city': 'New Orleans',
                    'state': 'LA',
                    'zip': '70122',
                },
                'transactions': [
                    {
                        'date': '2016-01-01',
                        'amount': '5.55',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-02-01',
                        'amount': '6.66',
                        'note': 'Bought something',
                    },
                    {
                        'date': '2016-03-01',
                        'amount': '7.77',
                        'note': 'Bought something',
                    },
                ],
            },
        ],
    },
]

@app.route('/')
def index():
    """Return index page."""
    featured_companies = COMPANIES[0:9]
    return render_template('index.html', companies=featured_companies)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Return sign in page."""
    if request.method == 'POST':
        for company in COMPANIES:
            if request.form['username'] == company['username'] and request.form['password'] == company['password']:
                session.username = request.form['username']
                session.index = int(company['index'])
                break
        return redirect("/dashboard/%d" % session.index, code=302)
    return render_template('login.html')

@app.route('/join', methods=['GET', 'POST'])
def join():
    """Return about page."""
    index = len(COMPANIES)
    if request.method == 'POST':
        business = {
            'index': index,
            'in_need': len(request.form.getlist('in_need')) > 0,
            'username': request.form['username'],
            'name': request.form['name'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'password': request.form['password'],
            'business_name': request.form['business_name'],
            'business_website': request.form['business_website'],
            'business_image': request.form['business_image'],
            'business_images': [request.form['business_image'], '/static/cake1.jpg', '/static/cake7.jpg'],
            'business_email': request.form['business_email'],
            'business_phone': request.form['business_phone'],
            'business_description': request.form['business_description'],
            'customers': [],
        }
        COMPANIES.append(business)
        return redirect("/dashboard/%d" % index , code=302)
    else:
        return render_template('join.html')

@app.route('/about')
def about():
    """Return about page."""
    return render_template('about.html')

@app.route('/add_customer/<index>', methods=['GET', 'POST'])
def add_customer(index):
    """Return add customer page."""
    customer_index = len(COMPANIES[int(index)]['customers'])
    if request.method == 'POST':
        customer = {
            'index': customer_index,
            'name': request.form['name'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'address': {
                'line1': request.form['address_line1'],
                'line2': request.form['address_line2'],
                'city': request.form['address_city'],
                'state': request.form['address_state'],
                'zip': request.form['address_zip'],
            },
            'transactions': [],
        }
        COMPANIES[int(index)]['customers'].append(customer)
        return render_template('customers.html', company=COMPANIES[int(index)])
    else:
        return render_template('add_customer.html', company=COMPANIES[int(index)])

@app.route('/company/<company_index>/customer/<customer_index>/txns')
def customer_txns(company_index, customer_index):
    """Return contact page."""
    return render_template('customer_txns.html', company=COMPANIES[int(company_index)], customer=COMPANIES[int(company_index)]['customers'][int(customer_index)])

@app.route('/contact')
def contact():
    """Return contact page."""
    return render_template('contact.html')

@app.route('/donate/<index>')
def donate(index):
    """Return donate page."""
    return render_template('newdon.html', company=COMPANIES[int(index)])

@app.route('/patronize/<index>')
def patronize(index):
    """Return patronize page."""
    return render_template('patronize12.html', company=COMPANIES[int(index)])

@app.route('/individual/<index>')
def individual(index):
    """Return businesses page."""
    return render_template('indVolForm.html', company=COMPANIES[int(index)])

@app.route('/ingroup/<index>')
def InGroup(index):
    """Return businesses page."""
    return render_template('inGroupForm.html', company=COMPANIES[int(index)])

@app.route('/volunteer/<index>')
def volunteer(index):
    """Return volunteer page."""
    return render_template('volunteer.html', company=COMPANIES[int(index)])

@app.route('/opportunities')
def opportunities():
    """Return opportunities page."""
    return render_template('opportunities.html')

@app.route('/opportunity')
def opportunity():
    """Return opportunity page."""
    return render_template('opportunity.html')

@app.route('/dashboard/<index>')
def dashboard(index):
    """Return dashboard page."""
    return render_template('dashboard.html', company=COMPANIES[int(index)])

@app.route('/services')
def services():
    """Return services page."""
    return render_template('services.html')

@app.route('/service')
def service():
    """Return service page."""
    return render_template('service.html')

@app.route('/businesses')
def businesses():
    """Return businesses page."""
    return render_template('businesses.html', companies=COMPANIES)

@app.route('/card/<index>')
def card(index):
    """Return card information page."""
    return render_template('cardInfo.html',company=COMPANIES[int(index)])

@app.route('/insurance/<index>')
def insurance(index):
    """Return businesses page."""
    return render_template('insurance.html', company=COMPANIES[int(index)])

@app.route('/doner/<index>')
def Doner(index):
    """Return businesses page."""
    return render_template('DonerContact.html', company=COMPANIES[int(index)])

@app.route('/risk/<index>')
def risk(index):
    """Return businesses page."""
    return render_template('risk.html', company=COMPANIES[int(index)])

@app.route('/business/<index>')
def business(index):
    """Return business page."""
    # TODO: check bounds here and redirect
    return render_template('business.html', company=COMPANIES[int(index)])

@app.route('/edit/<index>', methods=['GET', 'POST'])
def edit(index):
    """Return business page."""
    if request.method == 'POST':
        business = {
            'index': index,
            'username': request.form['username'],
            'name': request.form['name'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'password': request.form['password'],
            'in_need': len(request.form.getlist('in_need')) > 0,
            'business_name': request.form['business_name'],
            'business_website': request.form['business_website'],
            'business_image': request.form['business_image'],
            'business_email': request.form['business_email'],
            'business_phone': request.form['business_phone'],
            'business_address': {
                'line1': request.form['business_address_line1'],
                'line2': request.form['business_address_line2'],
                'city': request.form['business_address_city'],
                'state': request.form['business_address_state'],
                'zip': request.form['business_address_zip'],
            },
            'business_description': request.form['business_description'],
            'customers': COMPANIES[int(index)]['customers'],
        }
        COMPANIES[int(index)] = business
        return redirect("/dashboard/%d" % int(index) , code=302)
    else:
        return render_template('edit.html', company=COMPANIES[int(index)])

@app.route('/customers/<index>')
def customers(index):
    """Return business page."""
    # TODO: check bounds here and redirect
    return render_template('customers.html', company=COMPANIES[int(index)])

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
