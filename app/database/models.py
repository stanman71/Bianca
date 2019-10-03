from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


from app                         import app
from app.common                  import COMMON, STATUS, DATATYPE
from app.backend.file_management import WRITE_LOGFILE_SYSTEM, WRITE_PLANTS_DATAFILE, CREATE_PLANTS_DATAFILE, RENAME_PLANTS_DATAFILE, DELETE_PLANTS_DATAFILE

import datetime
import re

db = SQLAlchemy(app)

class Controller(db.Model):
    __tablename__   = 'controller'
    id              = db.Column(db.Integer, primary_key=True, autoincrement = True)
    device_ieeeAddr = db.Column(db.String(50), db.ForeignKey('devices.ieeeAddr')) 
    device          = db.relationship('Devices') 
    command_1       = db.Column(db.String(50))
    task_1          = db.Column(db.String(50))
    command_2       = db.Column(db.String(50))
    task_2          = db.Column(db.String(50))
    command_3       = db.Column(db.String(50))
    task_3          = db.Column(db.String(50))    
    command_4       = db.Column(db.String(50))
    task_4          = db.Column(db.String(50))
    command_5       = db.Column(db.String(50))
    task_5          = db.Column(db.String(50))
    command_6       = db.Column(db.String(50))
    task_6          = db.Column(db.String(50))   
    command_7       = db.Column(db.String(50))
    task_7          = db.Column(db.String(50))
    command_8       = db.Column(db.String(50))
    task_8          = db.Column(db.String(50))
    command_9       = db.Column(db.String(50))
    task_9          = db.Column(db.String(50))   
    collapse        = db.Column(db.String(50))        

class Devices(db.Model):
    __tablename__ = 'devices'
    id                            = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name                          = db.Column(db.String(50), unique=True)
    gateway                       = db.Column(db.String(50)) 
    ieeeAddr                      = db.Column(db.String(50), unique=True)  
    model                         = db.Column(db.String(50))
    device_type                   = db.Column(db.String(50))
    description                   = db.Column(db.String(200))
    input_values                  = db.Column(db.String(200))
    input_events                  = db.Column(db.String(200))
    commands                      = db.Column(db.String(200))    
    last_contact                  = db.Column(db.String(50))
    last_values                   = db.Column(db.String(200))  
    last_values_formated          = db.Column(db.String(200)) 
    exception_option              = db.Column(db.String(50)) 
    exception_setting             = db.Column(db.String(50))     
    exception_sensor_ieeeAddr     = db.Column(db.String(50))   
    exception_sensor_input_values = db.Column(db.String(50))     
    exception_value_1             = db.Column(db.String(50))
    exception_value_2             = db.Column(db.String(50))
    exception_value_3             = db.Column(db.String(50))       

class eMail(db.Model):
    __tablename__  = 'email'
    id             = db.Column(db.Integer, primary_key=True, autoincrement = True)
    server_address = db.Column(db.String(50))
    server_port    = db.Column(db.Integer)
    encoding       = db.Column(db.String(50))
    username       = db.Column(db.String(50))
    password       = db.Column(db.String(50)) 

class Host(db.Model):
    __tablename__ = 'host'
    id                = db.Column(db.Integer, primary_key=True, autoincrement = True)
    lan_dhcp          = db.Column(db.String(50), server_default=("True"))    
    lan_ip_address    = db.Column(db.String(50))
    lan_gateway       = db.Column(db.String(50))

class LED_Groups(db.Model):
    __tablename__         = 'led_groups'
    id                    = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name                  = db.Column(db.String(50), unique = True)
    led_ieeeAddr_1        = db.Column(db.String(50))
    led_name_1            = db.Column(db.String(50))
    led_device_type_1     = db.Column(db.String(50))
    active_led_2          = db.Column(db.String(50))
    led_ieeeAddr_2        = db.Column(db.String(50))           
    led_name_2            = db.Column(db.String(50))
    led_device_type_2     = db.Column(db.String(50))
    active_led_3          = db.Column(db.String(50))
    led_ieeeAddr_3        = db.Column(db.String(50))           
    led_name_3            = db.Column(db.String(50))
    led_device_type_3     = db.Column(db.String(50))
    active_led_4          = db.Column(db.String(50))
    led_ieeeAddr_4        = db.Column(db.String(50))       
    led_name_4            = db.Column(db.String(50))
    led_device_type_4     = db.Column(db.String(50))
    active_led_5          = db.Column(db.String(50))
    led_ieeeAddr_5        = db.Column(db.String(50))         
    led_name_5            = db.Column(db.String(50)) 
    led_device_type_5     = db.Column(db.String(50))
    active_led_6          = db.Column(db.String(50))
    led_ieeeAddr_6        = db.Column(db.String(50))
    led_name_6            = db.Column(db.String(50))
    led_device_type_6     = db.Column(db.String(50))
    active_led_7          = db.Column(db.String(50))
    led_ieeeAddr_7        = db.Column(db.String(50))
    led_name_7            = db.Column(db.String(50))
    led_device_type_7     = db.Column(db.String(50))
    active_led_8          = db.Column(db.String(50))
    led_ieeeAddr_8        = db.Column(db.String(50))
    led_name_8            = db.Column(db.String(50))
    led_device_type_8     = db.Column(db.String(50))
    active_led_9          = db.Column(db.String(50))
    led_ieeeAddr_9        = db.Column(db.String(50))
    led_name_9            = db.Column(db.String(50)) 
    led_device_type_9     = db.Column(db.String(50))
    collapse              = db.Column(db.String(50))    
    current_setting       = db.Column(db.String(50), server_default=("OFF"))
    current_brightness    = db.Column(db.Integer, server_default=("0"))

class LED_Scenes(db.Model):
    __tablename__ = 'led_scenes'
    id                    = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name                  = db.Column(db.String(50), unique = True) 
    hex_1                 = db.Column(db.String(50), server_default=("0"))
    color_temp_1          = db.Column(db.Integer, server_default=("100"))
    brightness_1          = db.Column(db.Integer, server_default=("254"))
    active_setting_2      = db.Column(db.String(50))
    red_2                 = db.Column(db.Integer, server_default=("0"))
    green_2               = db.Column(db.Integer, server_default=("0"))
    blue_2                = db.Column(db.Integer, server_default=("0"))
    color_temp_2          = db.Column(db.Integer, server_default=("100"))
    brightness_2          = db.Column(db.Integer, server_default=("254"))
    active_setting_3      = db.Column(db.String(50))
    red_3                 = db.Column(db.Integer, server_default=("0"))
    green_3               = db.Column(db.Integer, server_default=("0"))
    blue_3                = db.Column(db.Integer, server_default=("0"))
    color_temp_3          = db.Column(db.Integer, server_default=("100"))
    brightness_3          = db.Column(db.Integer, server_default=("254"))
    active_setting_4      = db.Column(db.String(50))
    red_4                 = db.Column(db.Integer, server_default=("0"))
    green_4               = db.Column(db.Integer, server_default=("0"))
    blue_4                = db.Column(db.Integer, server_default=("0"))
    color_temp_4          = db.Column(db.Integer, server_default=("100"))
    brightness_4          = db.Column(db.Integer, server_default=("254"))
    active_setting_5      = db.Column(db.String(50))
    red_5                 = db.Column(db.Integer, server_default=("0"))
    green_5               = db.Column(db.Integer, server_default=("0"))
    blue_5                = db.Column(db.Integer, server_default=("0"))
    color_temp_5          = db.Column(db.Integer, server_default=("100"))
    brightness_5          = db.Column(db.Integer, server_default=("254"))        
    active_setting_6      = db.Column(db.String(50))
    red_6                 = db.Column(db.Integer, server_default=("0"))
    green_6               = db.Column(db.Integer, server_default=("0"))
    blue_6                = db.Column(db.Integer, server_default=("0"))
    color_temp_6          = db.Column(db.Integer, server_default=("100"))
    brightness_6          = db.Column(db.Integer, server_default=("254"))
    active_setting_7      = db.Column(db.String(50))
    red_7                 = db.Column(db.Integer, server_default=("0"))
    green_7               = db.Column(db.Integer, server_default=("0"))
    blue_7                = db.Column(db.Integer, server_default=("0"))
    color_temp_7          = db.Column(db.Integer, server_default=("100"))
    brightness_7          = db.Column(db.Integer, server_default=("254"))
    active_setting_8      = db.Column(db.String(50))
    red_8                 = db.Column(db.Integer, server_default=("0"))
    green_8               = db.Column(db.Integer, server_default=("0"))
    blue_8                = db.Column(db.Integer, server_default=("0"))
    color_temp_8          = db.Column(db.Integer, server_default=("100"))
    brightness_8          = db.Column(db.Integer, server_default=("254"))
    active_setting_9      = db.Column(db.String(50))
    red_9                 = db.Column(db.Integer, server_default=("0"))
    green_9               = db.Column(db.Integer, server_default=("0"))
    blue_9                = db.Column(db.Integer, server_default=("0"))
    color_temp_9          = db.Column(db.Integer, server_default=("100"))
    brightness_9          = db.Column(db.Integer, server_default=("254"))   
    collapse              = db.Column(db.String(50))        

class MQTT_Broker(db.Model):
    __tablename__     = 'mqtt_broker'
    id                = db.Column(db.Integer, primary_key=True, autoincrement = True)
    broker            = db.Column(db.String(50))
    user              = db.Column(db.String(50))
    password          = db.Column(db.String(50))
    previous_broker   = db.Column(db.String(50))
    previous_user     = db.Column(db.String(50))
    previous_password = db.Column(db.String(50))    

class Plants(db.Model):
    __tablename__  = 'plants'
    id                     = db.Column(db.Integer, primary_key=True, autoincrement = True)   
    name                   = db.Column(db.String(50), unique=True)
    device_ieeeAddr        = db.Column(db.String(50), db.ForeignKey('devices.ieeeAddr'))   
    device                 = db.relationship('Devices')  
    group                  = db.Column(db.Integer)        
    pump_duration_auto     = db.Column(db.Integer)  
    pump_duration_manually = db.Column(db.Integer)            
    moisture_level         = db.Column(db.String(50)) 

class Scheduler_Tasks(db.Model):
    __tablename__ = 'scheduler_tasks'
    id     = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name   = db.Column(db.String(50), unique=True)
    task   = db.Column(db.String(50))  
    hour   = db.Column(db.Integer)  
    minute = db.Column(db.Integer)         
    pause  = db.Column(db.String(50))

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id                 = db.Column(db.Integer,     primary_key=True)
    username           = db.Column(db.String(64),  unique = True)
    email              = db.Column(db.String(120), unique = True)
    role               = db.Column(db.String(50))   
    password           = db.Column(db.String(100))
    email_notification = db.Column(db.String(20))

class ZigBee2MQTT(db.Model):
    __tablename__ = 'zigbee2mqtt'
    id      = db.Column(db.Integer, primary_key=True, autoincrement = True)
    pairing = db.Column(db.String(50))


""" ################################ """
""" ################################ """
""" create tables and default values """
""" ################################ """
""" ################################ """


# create all database tables
db.create_all()


# create default email
if eMail.query.filter_by().first() is None:
    email = eMail(
        id = 1,
    )
    db.session.add(email)
    db.session.commit()


# create default host settings
if Host.query.filter_by().first() is None:
    host = Host(
    )
    db.session.add(host)
    db.session.commit()


# create default mqtt broker settings
if MQTT_Broker.query.filter_by().first() is None:
    mqtt_broker = MQTT_Broker(
        broker   = "localhost",
        user     = "",
        password = "",
    )
    db.session.add(mqtt_broker)
    db.session.commit()


# create default scheduler settings
if Scheduler_Tasks.query.filter_by().first() is None:
    scheduler_task_plants_group_1 = Scheduler_Tasks(
        name   = "plants_group_1",
    )
    db.session.add(scheduler_task_plants_group_1)

    scheduler_task_plants_group_2 = Scheduler_Tasks(
        name   = "plants_group_2",
    )
    db.session.add(scheduler_task_plants_group_2)

    scheduler_task_plants_group_3 = Scheduler_Tasks(
        name   = "plants_group_3",
    )
    db.session.add(scheduler_task_plants_group_3)

    scheduler_task_update_devices = Scheduler_Tasks(
        name   = "update_devices",
        task   = "update_devices",
        hour   = "*",
        minute = "15",       
    )
    db.session.add(scheduler_task_update_devices)

    scheduler_task_backup = Scheduler_Tasks(
        name   = "backup_database",
        task   = "create_database_backup",
        hour   = "0",
        minute = "0",        
    )
    db.session.add(scheduler_task_backup)
    db.session.commit()

# create default user
if User.query.filter_by(username='admin').first() is None:
    user = User(
        username           = "admin",
        email              = "member@example.com",
        role               = "administrator",
        password           = "sha256$OeDkVenT$bc8d974603b713097e69fc3efa1132991bfb425c59ec00f207e4b009b91f4339",    
        email_notification = "True"
    )           
    
    db.session.add(user)
    db.session.commit()


# create default zigbee2mqtt settings
if ZigBee2MQTT.query.filter_by().first() is None:
    zigbee2mqtt = ZigBee2MQTT(
        pairing = "False",
    )
    db.session.add(zigbee2mqtt)
    db.session.commit()


""" ################## """
""" ################## """
"""     Controller     """
""" ################## """
""" ################## """


def GET_CONTROLLER_BY_ID(id):
    return Controller.query.filter_by(id=id).first()
    
    
def GET_CONTROLLER_BY_IEEEADDR(device_ieeeAddr):
    return Controller.query.filter_by(device_ieeeAddr=device_ieeeAddr).first()
    
    
def GET_ALL_CONTROLLER():   
    return Controller.query.all()
        

def ADD_CONTROLLER(device_ieeeAddr):
    # controller exist ?
    if not GET_CONTROLLER_BY_IEEEADDR(device_ieeeAddr):
        
        # find a unused id
        for i in range(1,21):
            if Controller.query.filter_by(id=i).first():
                pass
            else:
                # add new controller
                controller = Controller(
                                        id = i,
                                        device_ieeeAddr = device_ieeeAddr,
                                        )
                db.session.add(controller)
                db.session.commit()
                
                UPDATE_CONTROLLER_EVENTS()
                
                controller_name = GET_DEVICE_BY_IEEEADDR(device_ieeeAddr).name

                WRITE_LOGFILE_SYSTEM("DATABASE", "Controller - " + controller_name + " | added")  

                return True


def UPDATE_CONTROLLER_EVENTS(): 
    
    for controller in GET_ALL_CONTROLLER():
    
        device_input_events = GET_DEVICE_BY_IEEEADDR(controller.device_ieeeAddr).input_events
        device_input_events = device_input_events.split(" ")

        try:
            device_events        = device_input_events[0].replace(" ","")
            controller.command_1 = device_events
        except:
            controller.command_1 = "None"
        try:
            device_events        = device_input_events[1].replace(" ","")
            controller.command_2 = device_events
        except:
            controller.command_2 = "None"
        try:
            device_events        = device_input_events[2].replace(" ","")
            controller.command_3 = device_events
        except:
            controller.command_3 = "None"
        try:
            device_events        = device_input_events[3].replace(" ","")
            controller.command_4 = device_events
        except:
            controller.command_4 = "None"
        try:
            device_events        = device_input_events[4].replace(" ","")
            controller.command_5 = device_events
        except:
            controller.command_5 = "None"
        try:
            device_events        = device_input_events[5].replace(" ","")
            controller.command_6 = device_events
        except:
            controller.command_6 = "None"            
        try:
            device_events        = device_input_events[6].replace(" ","")
            controller.command_7 = device_events
        except:
            controller.command_7 = "None"
        try:
            device_events        = device_input_events[7].replace(" ","")
            controller.command_8 = device_events
        except:
            controller.command_8 = "None"
        try:
            device_events        = device_input_events[8].replace(" ","")
            controller.command_9 = device_events
        except:
            controller.command_9 = "None"      

        db.session.commit()


def SET_CONTROLLER_COLLAPSE_OPEN(id):
    list_controller = Controller.query.all()
    
    for controller in list_controller:
        controller.collapse = ""
        db.session.commit()   
  
    entry = Controller.query.filter_by(id=id).first()
    
    entry.collapse = "True"
    db.session.commit()   


def RESET_CONTROLLER_COLLAPSE():
    list_controller = Controller.query.all()
    
    for controller in list_controller:
        controller.collapse = ""
        db.session.commit()   


def SET_CONTROLLER_TASKS(id, task_1 = "", task_2 = "", task_3 = "", task_4 = "", task_5 = "",
                             task_6 = "", task_7 = "", task_8 = "", task_9 = ""):  

    entry = Controller.query.filter_by(id=id).first()

    if (entry.task_1 != task_1 or entry.task_2 != task_2 or entry.task_3 != task_3 or entry.task_4 != task_4 or entry.task_5 != task_5 or 
        entry.task_6 != task_6 or entry.task_7 != task_7 or entry.task_8 != task_8 or entry.task_9 != task_9):

        entry.task_1 = task_1
        entry.task_2 = task_2
        entry.task_3 = task_3   
        entry.task_4 = task_4
        entry.task_5 = task_5
        entry.task_6 = task_6     
        entry.task_7 = task_7
        entry.task_8 = task_8
        entry.task_9 = task_9               
        db.session.commit() 

        return True


def CHANGE_CONTROLLER_POSITION(id, direction):
    
    if direction == "up":
        controller_list = GET_ALL_CONTROLLER()
        controller_list = controller_list[::-1]
        
        for controller in controller_list:
            
            if controller.id < id:     
                new_id = controller.id
                
                # change ids
                controller_1 = GET_CONTROLLER_BY_ID(id)
                controller_2 = GET_CONTROLLER_BY_ID(new_id)
                
                controller_1.id = 99
                db.session.commit()
                
                controller_2.id = id
                controller_1.id = new_id
                db.session.commit()
                
                return 

    if direction == "down":
        for controller in GET_ALL_CONTROLLER():
            if controller.id > id:       
                new_id = controller.id
                
                # change ids
                controller_1 = GET_CONTROLLER_BY_ID(id)
                controller_2 = GET_CONTROLLER_BY_ID(new_id)
                
                controller_1.id = 99
                db.session.commit()
                
                controller_2.id = id
                controller_1.id = new_id
                db.session.commit()
                
                return 


def DELETE_CONTROLLER(device_ieeeAddr):
    Controller.query.filter_by(device_ieeeAddr=device_ieeeAddr).delete()
    db.session.commit()


""" ################### """
""" ################### """
"""       devices       """
""" ################### """
""" ################### """


def GET_DEVICE_BY_ID(id):
    return Devices.query.filter_by(id=id).first()


def GET_DEVICE_BY_NAME(name):
    for device in Devices.query.all():
        
        if device.name.lower() == name.lower():
            return device 
    
    
def GET_DEVICE_BY_IEEEADDR(ieeeAddr):
    return Devices.query.filter_by(ieeeAddr=ieeeAddr).first()   


def GET_ALL_DEVICES(selector):
    device_list = []
    devices     = Devices.query.all()
  
    if selector == "":
        for device in devices:
            
            device_list.append(device)     

    if selector == "controller":
        for device in devices:
            if device.device_type == "controller":
                
                device_list.append(device)      
 
    if selector == "devices":
        for device in devices:
            if (device.device_type == "power_switch"):
                
                device_list.append(device)      
  
    if selector == "heaters":
        for device in devices:
            if device.device_type == "heater":
                
                device_list.append(device)          

    if selector == "led":
        for device in devices:
            if (device.device_type == "led_rgb" or 
                device.device_type == "led_white" or 
                device.device_type == "led_simple"):
                    
                device_list.append(device)    
                
    if selector == "sensors":
        for device in devices:
            
            if (device.device_type == "sensor_passiv" or 
                device.device_type == "sensor_active" or 
                device.device_type == "sensor_contact" or
                device.device_type == "watering_controller"):
                
                device_list.append(device)   
   
    if selector == "watering_controller":
        for device in devices:
            if device.device_type == "watering_controller":
                
                device_list.append(device)       
    
    return device_list    
        

def ADD_DEVICE(name, gateway, ieeeAddr, model = "", device_type = "", description = "", 
               input_values = "", input_events = "", commands = "", last_contact = ""):
        
    # path exist ?
    if not GET_DEVICE_BY_IEEEADDR(ieeeAddr):   
            
        # find a unused id
        for i in range(1,51):
            
            if Devices.query.filter_by(id=i).first():
                pass
                
            else:
                # add the new device            
                device = Devices(
                        id               = i,
                        name             = name,
                        gateway          = gateway,                    
                        ieeeAddr         = ieeeAddr,
                        model            = model,
                        device_type      = device_type,
                        description      = description,
                        input_values     = str(input_values),
                        input_events     = str(input_events),
                        commands         = str(commands),                    
                        last_contact     = last_contact,
                        exception_option = "None"
                        )
                        
                db.session.add(device)
                db.session.commit()
                
                SET_DEVICE_LAST_CONTACT(ieeeAddr)   

                if device_type == "controller":
                    ADD_CONTROLLER(ieeeAddr)
                
                return True

        return "Gerätelimit erreicht (50)"                           
                
    else:
        SET_DEVICE_LAST_CONTACT(ieeeAddr)  


def SET_DEVICE_NAME(ieeeAddr, new_name):
    entry = Devices.query.filter_by(ieeeAddr=ieeeAddr).first()
    
    WRITE_LOGFILE_SYSTEM("DATABASE", "Device | " + entry.name + " | Name changed" + " || Name - " + new_name)
    
    entry.name = new_name
    db.session.commit()       


def SET_DEVICE_LAST_CONTACT(ieeeAddr):
    timestamp = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) 
    entry = Devices.query.filter_by(ieeeAddr=ieeeAddr).first()
    entry.last_contact = timestamp
    db.session.commit()       


def SET_DEVICE_LAST_VALUES(ieeeAddr, last_values):
    entry = Devices.query.filter_by(ieeeAddr=ieeeAddr).first()
    
    last_values_formated = last_values.replace("{","")
    last_values_formated = last_values_formated.replace("}","")
    last_values_formated = last_values_formated.replace('"',"")
    last_values_formated = last_values_formated.replace(":",": ")
    last_values_formated = last_values_formated.replace(",",", ")
    
    timestamp = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    entry.last_values          = last_values
    entry.last_values_formated = last_values_formated
    entry.last_contact         = timestamp
    db.session.commit()   

    # write data_file
    for plant in GET_ALL_PLANTS():
        if plant.device_ieeeAddr == ieeeAddr:
            device_name = GET_DEVICE_BY_IEEEADDR(ieeeAddr).name
            
            # extract numbers
            list_values = re.findall(r'\b\d+\b', last_values_formated)
            WRITE_PLANTS_DATAFILE(plant.name, device_name, list_values[0], list_values[1], list_values[2])


def UPDATE_DEVICE(id, name, gateway, model, device_type = "", description = "", input_values = "", input_events = "", commands = ""):
    entry = Devices.query.filter_by(id=id).first()
    
    # values changed ?
    if (entry.name != name or entry.model != model or entry.device_type != device_type or entry.description != description 
        or entry.input_values != input_values or entry.input_events != input_events or entry.commands != commands):
        
        entry.model           = model
        entry.device_type     = device_type
        entry.description     = description
        entry.input_values    = str(input_values)
        entry.input_events    = str(input_events)
        entry.commands        = str(commands)        
        
        WRITE_LOGFILE_SYSTEM("DATABASE", "Device - " + entry.name + " | changed" + 
                             " || Name - " + name + 
                             " | ieeeAddr - " + entry.ieeeAddr + 
                             " | Model - " + entry.model +
                             " | device_type - " + entry.device_type +
                             " | description - " + entry.description +
                             " | Input_values - " + str(input_values) + 
                             " | Input_events - " + str(input_events) + 
                             " | Commands - " + str(commands))

        entry.name = name
        db.session.commit()    
   
        if device_type == "controller":
            ADD_CONTROLLER(GET_DEVICE_BY_ID(id).ieeeAddr)
            UPDATE_CONTROLLER_EVENTS()


def UPDATE_DEVICE_EXCEPTION_SENSOR_NAMES():

    try:
        for device in GET_ALL_DEVICES("device"):
            
            if device.exception_sensor_ieeeAddr != "None":
                device.exception_option = GET_DEVICE_BY_IEEEADDR(device.exception_sensor_ieeeAddr).name
            
        db.session.commit()
        
    except:
        pass


def SET_DEVICE_EXCEPTION(ieeeAddr, exception_option, exception_setting, exception_sensor_ieeeAddr, 
                         exception_sensor_input_values, exception_value_1, exception_value_2, exception_value_3):
              
    entry = Devices.query.filter_by(ieeeAddr=ieeeAddr).first()
             
    # values changed ?
    if (entry.exception_option != exception_option or entry.exception_setting != exception_setting or
        entry.exception_sensor_ieeeAddr != exception_sensor_ieeeAddr or 
        entry.exception_sensor_input_values != exception_sensor_input_values or 
        entry.exception_value_1 != exception_value_1 or entry.exception_value_2 != exception_value_2 or 
        entry.exception_value_3 != exception_value_3):              
                                         
        entry.exception_option              = exception_option
        entry.exception_setting             = exception_setting          
        entry.exception_sensor_ieeeAddr     = exception_sensor_ieeeAddr
        entry.exception_sensor_input_values = exception_sensor_input_values
        entry.exception_value_1             = exception_value_1
        entry.exception_value_2             = exception_value_2 
        entry.exception_value_3             = exception_value_3         
        
        db.session.commit()  
        
        WRITE_LOGFILE_SYSTEM("DATABASE", "Device - " + entry.name + " | Exception Settings changed" +
                             " || Exception - " + entry.exception_option +
                             " | Exception Setting - " + entry.exception_setting +                          
                             " | Exception ieeeAddr - " + entry.exception_sensor_ieeeAddr +
                             " | Exception Value 1 - " + entry.exception_value_1 +
                             " | Exception Value 2 - " + entry.exception_value_2 +      
                             " | Exception Value 3 - " + entry.exception_value_3) 

        return True

    
def CHANGE_DEVICE_POSITION(id, direction):
    
    if direction == "up":
        device_list = GET_ALL_DEVICES("")
        device_list = device_list[::-1]
        
        for device in device_list:
            
            if device.id < id:
                
                new_id = device.id
                
                # change ids
                device_1 = GET_DEVICE_BY_ID(id)
                device_2 = GET_DEVICE_BY_ID(new_id)
                
                device_1.id = 99
                db.session.commit()
                
                device_2.id = id
                device_1.id = new_id
                db.session.commit()
                
                return 

    if direction == "down":
        for device in GET_ALL_DEVICES(""):
            if device.id > id:
                
                new_id = device.id
                
                # change ids
                device_1 = GET_DEVICE_BY_ID(id)
                device_2 = GET_DEVICE_BY_ID(new_id)
                
                device_1.id = 99
                db.session.commit()
                
                device_2.id = id
                device_1.id = new_id
                db.session.commit()
                
                return 


def DELETE_DEVICE(ieeeAddr):
    error_list = ""

    # check plants
    entries = GET_ALL_PLANTS()
    for entry in entries:
        if entry.device_ieeeAddr == ieeeAddr:
            device = GET_DEVICE_BY_IEEEADDR(ieeeAddr)
            error_list = error_list + "," + device.name + " eingetragen in Bewässung"
    

    """
    # check scheduler sensor
    entries = GET_ALL_SCHEDULER_TASKS()
    for entry in entries:
        if (entry.device_ieeeAddr_1 == ieeeAddr) or (entry.device_ieeeAddr_2 == ieeeAddr) or (entry.device_ieeeAddr_3 == ieeeAddr):
            device = GET_DEVICE_BY_IEEEADDR(ieeeAddr)
            error_list = error_list + "," + device.name + " eingetragen in Aufgabenplanung"
    
    # check sensordata
    entries = GET_ALL_SENSORDATA_JOBS()
    for entry in entries:
        if entry.device_ieeeAddr == ieeeAddr:
            device = GET_DEVICE_BY_IEEEADDR(ieeeAddr)
            error_list = error_list + "," + device.name + " eingetragen in Sensordaten / Jobs"
        
    # check speechcontrol
    entries = GET_ALL_SPEECHCONTROL_DEVICE_TASKS()
    for entry in entries:
        if entry.device_ieeeAddr == ieeeAddr:
            device = GET_DEVICE_BY_IEEEADDR(ieeeAddr)
            error_list = error_list + "," + device.name + " eingetragen in System / Sprachsteuerung"            
        
    # check led groups
    entries = GET_ALL_LED_GROUPS()
    for entry in entries:
        if entry.led_ieeeAddr_1 == ieeeAddr:
            device = GET_DEVICE_BY_IEEEADDR(ieeeAddr)
            error_list = error_list + "," + device.name + " eingetragen in LED / Gruppen"
        if entry.led_ieeeAddr_2 == ieeeAddr:
            device = GET_DEVICE_BY_IEEEADDR(ieeeAddr)
            error_list = error_list + "," + device.name + " eingetragen in LED / Gruppen"
        if entry.led_ieeeAddr_3 == ieeeAddr:
            device = GET_DEVICE_BY_IEEEADDR(ieeeAddr)
            error_list = error_list + "," + device.name + " eingetragen in LED / Gruppen" 
        if entry.led_ieeeAddr_4 == ieeeAddr:
            device = GET_DEVICE_BY_IEEEADDR(ieeeAddr)
            error_list = error_list + "," + device.name + " eingetragen in LED / Gruppen"
        if entry.led_ieeeAddr_5 == ieeeAddr:
            device = GET_DEVICE_BY_IEEEADDR(ieeeAddr)
            error_list = error_list + "," + device.name + " eingetragen in LED / Gruppen"
        if entry.led_ieeeAddr_6 == ieeeAddr:
            device = GET_DEVICE_BY_IEEEADDR(ieeeAddr)
            error_list = error_list + "," + device.name + " eingetragen in LED / Gruppen"
        if entry.led_ieeeAddr_7 == ieeeAddr:
            device = GET_DEVICE_BY_IEEEADDR(ieeeAddr)
            error_list = error_list + "," + device.name + " eingetragen in LED / Gruppen"
        if entry.led_ieeeAddr_8 == ieeeAddr:
            device = GET_DEVICE_BY_IEEEADDR(ieeeAddr)
            error_list = error_list + "," + device.name + " eingetragen in LED / Gruppen"
        if entry.led_ieeeAddr_9 == ieeeAddr:
            device = GET_DEVICE_BY_IEEEADDR(ieeeAddr)
            error_list = error_list + "," + device.name + " eingetragen in LED / Gruppen"            
        """


    if error_list != "":
        return error_list[1:]   
               
    else:
        
        try:
            device      = GET_DEVICE_BY_IEEEADDR(ieeeAddr)
            device_name = device.name
            
            if device.device_type == "controller":
                DELETE_CONTROLLER(ieeeAddr)

            Devices.query.filter_by(ieeeAddr=ieeeAddr).delete()
            db.session.commit() 
            
            WRITE_LOGFILE_SYSTEM("DATABASE", "Device - " + device_name + " | deleted")
                        
            return True

        except Exception as e:
            return e


""" ################## """
""" ################## """
"""        eMail       """
""" ################## """
""" ################## """


def GET_EMAIL_SETTINGS():   
    return eMail.query.filter_by().first()


def GET_EMAIL_ADDRESSES(address_type): 
    if address_type == "TEST":
        mail_list = []
        mail_list.append(eMail.query.filter_by().first().username)
        return mail_list

    if address_type == "NOTIFICATION":
        mail_list = []
        users = User.query.all()
        for user in users:
            if user.email_notification == "True":
                mail_list.append(user.email)
        return mail_list


def SET_EMAIL_SETTINGS(server_address, server_port, encoding, username, password): 
    entry = eMail.query.filter_by().first()

    if (entry.server_address != server_address or entry.server_port != server_port or entry.encoding != encoding or entry.username != username or entry.password != password):

        entry.server_address = server_address
        entry.server_port    = server_port
        entry.encoding       = encoding
        entry.username       = username
        entry.password       = password
        db.session.commit()
        
        WRITE_LOGFILE_SYSTEM("DATABASE", "eMail | Server Settings | changed")
        
        return True


""" ################### """
""" ################### """
"""         host        """
""" ################### """
""" ################### """


def GET_HOST_NETWORK():
    return Host.query.filter_by().first()


def UPDATE_HOST_INTERFACE_LAN_DHCP(lan_dhcp):
    entry = Host.query.filter_by().first()
    
    # values changed ?
    if entry.lan_dhcp != lan_dhcp:   
    
        entry.lan_dhcp        = lan_dhcp    
        db.session.commit()
        
        WRITE_LOGFILE_SYSTEM("DATABASE", "Host | Network settings changed " +
                             "| DHCP LAN - " +  str(lan_dhcp))    

        return True 


def UPDATE_HOST_INTERFACE_LAN(lan_ip_address, lan_gateway):
    entry = Host.query.filter_by().first()
    
    # values changed ?
    if entry.lan_ip_address != lan_ip_address or entry.lan_gateway != lan_gateway:   
     
        entry.lan_ip_address  = lan_ip_address
        entry.lan_gateway     = lan_gateway  
        db.session.commit()
        
        WRITE_LOGFILE_SYSTEM("DATABASE", "Host | Network settings changed " +
                             "| LAN - " + str(lan_ip_address) + " : " + str(lan_gateway)) 

        return True


""" ################### """
""" ################### """
"""     led groups      """
""" ################### """
""" ################### """


def GET_ALL_LED_GROUPS():
    return LED_Groups.query.all()   
  
    
def GET_ALL_ACTIVE_LED_GROUPS():
    list_active_groups = []

    for group in LED_Groups.query.all():
        if group.led_ieeeAddr_1 != None and group.led_ieeeAddr_1 != "None":
            list_active_groups.append(group)
            
    return list_active_groups
          

def GET_LED_GROUP_BY_ID(id):
    return LED_Groups.query.filter_by(id=id).first()


def GET_LED_GROUP_BY_NAME(name):
    for group in LED_Groups.query.all():
        
        if group.name.lower() == name.lower():
            return group
        

def ADD_LED_GROUP(name):

    # find a unused id
    for i in range(1,21):
        if LED_Groups.query.filter_by(id=i).first():
            pass
        else:
            # add the new program
            group = LED_Groups(
                    id = i,
                    name = name,
                )
            db.session.add(group)
            db.session.commit()

            RESET_LED_GROUP_ERRORS()

            WRITE_LOGFILE_SYSTEM("DATABASE", "LED | Group - " + name + " | added")  

            return True

    return "Gruppenlimit erreicht (20)"


def SET_LED_GROUP(id, name, led_ieeeAddr_1, led_name_1, led_device_type_1, 
                            led_ieeeAddr_2, led_name_2, led_device_type_2,
                            led_ieeeAddr_3, led_name_3, led_device_type_3,
                            led_ieeeAddr_4, led_name_4, led_device_type_4,
                            led_ieeeAddr_5, led_name_5, led_device_type_5,
                            led_ieeeAddr_6, led_name_6, led_device_type_6,
                            led_ieeeAddr_7, led_name_7, led_device_type_7,
                            led_ieeeAddr_8, led_name_8, led_device_type_8,
                            led_ieeeAddr_9, led_name_9, led_device_type_9):

    entry = LED_Groups.query.filter_by(id=id).first()

    if (entry.led_ieeeAddr_1 != led_ieeeAddr_1 or entry.led_name_1 != led_name_1 or entry.led_device_type_1 != led_device_type_1 or 
        entry.led_ieeeAddr_2 != led_ieeeAddr_2 or entry.led_name_2 != led_name_2 or entry.led_device_type_2 != led_device_type_2 or
        entry.led_ieeeAddr_3 != led_ieeeAddr_3 or entry.led_name_3 != led_name_3 or entry.led_device_type_3 != led_device_type_3 or
        entry.led_ieeeAddr_4 != led_ieeeAddr_4 or entry.led_name_4 != led_name_4 or entry.led_device_type_4 != led_device_type_4 or
        entry.led_ieeeAddr_5 != led_ieeeAddr_5 or entry.led_name_5 != led_name_5 or entry.led_device_type_5 != led_device_type_5 or
        entry.led_ieeeAddr_6 != led_ieeeAddr_6 or entry.led_name_6 != led_name_6 or entry.led_device_type_6 != led_device_type_6 or
        entry.led_ieeeAddr_7 != led_ieeeAddr_7 or entry.led_name_7 != led_name_7 or entry.led_device_type_7 != led_device_type_7 or
        entry.led_ieeeAddr_8 != led_ieeeAddr_8 or entry.led_name_8 != led_name_8 or entry.led_device_type_8 != led_device_type_8 or
        entry.led_ieeeAddr_9 != led_ieeeAddr_9 or entry.led_name_9 != led_name_9 or entry.led_device_type_9 != led_device_type_9):

        entry.name = name
        
        entry.led_ieeeAddr_1    = led_ieeeAddr_1
        entry.led_name_1        = led_name_1
        entry.led_device_type_1 = led_device_type_1
        entry.led_ieeeAddr_2    = led_ieeeAddr_2
        entry.led_name_2        = led_name_2
        entry.led_device_type_2 = led_device_type_2 
        entry.led_ieeeAddr_3    = led_ieeeAddr_3
        entry.led_name_3        = led_name_3
        entry.led_device_type_3 = led_device_type_3
        entry.led_ieeeAddr_4    = led_ieeeAddr_4
        entry.led_name_4        = led_name_4
        entry.led_device_type_4 = led_device_type_4
        entry.led_ieeeAddr_5    = led_ieeeAddr_5
        entry.led_name_5        = led_name_5
        entry.led_device_type_5 = led_device_type_5
        entry.led_ieeeAddr_6    = led_ieeeAddr_6
        entry.led_name_6        = led_name_6
        entry.led_device_type_6 = led_device_type_6 
        entry.led_ieeeAddr_7    = led_ieeeAddr_7
        entry.led_name_7        = led_name_7
        entry.led_device_type_7 = led_device_type_7
        entry.led_ieeeAddr_8    = led_ieeeAddr_8
        entry.led_name_8        = led_name_8
        entry.led_device_type_8 = led_device_type_8
        entry.led_ieeeAddr_9    = led_ieeeAddr_9
        entry.led_name_9        = led_name_9
        entry.led_device_type_9 = led_device_type_9
        
        db.session.commit()  

        WRITE_LOGFILE_SYSTEM("DATABASE", "LED | Group - " + name + " | Settings changed")  

        return True 


def SET_LED_GROUP_COLLAPSE_OPEN(id):
    list_led_groups = LED_Groups.query.all()
    
    for led_group in list_led_groups:
        led_group.collapse = ""
        db.session.commit()   
  
    entry = LED_Groups.query.filter_by(id=id).first()
    
    entry.collapse = "True"
    db.session.commit()   


def RESET_LED_GROUP_COLLAPSE():
    list_led_groups = LED_Groups.query.all()
    
    for led_group in list_led_groups:
        led_group.collapse = ""
        db.session.commit()   


def SET_LED_GROUP_NAME(id, name):
    entry = LED_Groups.query.filter_by(id=id).first()
    entry.name = name
       
    db.session.commit()  


def SET_LED_GROUP_CURRENT_SETTING(id, current_setting):
    entry = LED_Groups.query.filter_by(id=id).first()
    entry.current_setting = current_setting     
    db.session.commit()  


def SET_LED_GROUP_CURRENT_BRIGHTNESS(id, current_brightness):
    entry = LED_Groups.query.filter_by(id=id).first()
    entry.current_brightness = current_brightness     
    db.session.commit()  


def UPDATE_LED_GROUP_LED_NAMES():
    groups = GET_ALL_LED_GROUPS()
    
    for group in groups:
        
        entry = LED_Groups.query.filter_by(id=group.id).first()
        
        try:
            entry.led_name_1        = GET_MQTT_DEVICE_BY_IEEEADDR(entry.led_ieeeAddr_1).name
            entry.led_device_type_1 = GET_MQTT_DEVICE_BY_IEEEADDR(entry.led_ieeeAddr_1).device_type
        except:
            pass
        try:
            entry.led_name_2        = GET_MQTT_DEVICE_BY_IEEEADDR(entry.led_ieeeAddr_2).name
            entry.led_device_type_2 = GET_MQTT_DEVICE_BY_IEEEADDR(entry.led_ieeeAddr_2).device_type
        except:
            pass
        try:
            entry.led_name_3        = GET_MQTT_DEVICE_BY_IEEEADDR(entry.led_ieeeAddr_3).name
            entry.led_device_type_3 = GET_MQTT_DEVICE_BY_IEEEADDR(entry.led_ieeeAddr_3).device_type
        except:
            pass
        try:
            entry.led_name_4        = GET_MQTT_DEVICE_BY_IEEEADDR(entry.led_ieeeAddr_4).name
            entry.led_device_type_4 = GET_MQTT_DEVICE_BY_IEEEADDR(entry.led_ieeeAddr_4).device_type
        except:
            pass
        try:
            entry.led_name_5        = GET_MQTT_DEVICE_BY_IEEEADDR(entry.led_ieeeAddr_5).name
            entry.led_device_type_5 = GET_MQTT_DEVICE_BY_IEEEADDR(entry.led_ieeeAddr_5).device_type
        except:
            pass
        try:
            entry.led_name_6        = GET_MQTT_DEVICE_BY_IEEEADDR(entry.led_ieeeAddr_6).name
            entry.led_device_type_6 = GET_MQTT_DEVICE_BY_IEEEADDR(entry.led_ieeeAddr_6).device_type
        except:
            pass
        try:
            entry.led_name_7        = GET_MQTT_DEVICE_BY_IEEEADDR(entry.led_ieeeAddr_7).name
            entry.led_device_type_7 = GET_MQTT_DEVICE_BY_IEEEADDR(entry.led_ieeeAddr_7).device_type
        except:
            pass
        try:
            entry.led_name_8        = GET_MQTT_DEVICE_BY_IEEEADDR(entry.led_ieeeAddr_8).name
            entry.led_device_type_8 = GET_MQTT_DEVICE_BY_IEEEADDR(entry.led_ieeeAddr_8).device_type
        except:
            pass
        try:
            entry.led_name_9        = GET_MQTT_DEVICE_BY_IEEEADDR(entry.led_ieeeAddr_9).name
            entry.led_device_type_9 = GET_MQTT_DEVICE_BY_IEEEADDR(entry.led_ieeeAddr_9).device_type
        except:
            pass            
        
    db.session.commit()


def ADD_LED_GROUP_LED(id):
    entry = LED_Groups.query.filter_by(id=id).first()

    if entry.active_led_2 != "True":
        entry.active_led_2 = "True"
        db.session.commit()
        return
    if entry.active_led_3 != "True":
        entry.active_led_3 = "True"
        db.session.commit()
        return
    if entry.active_led_4 != "True":
        entry.active_led_4 = "True"
        db.session.commit()
        return
    if entry.active_led_5 != "True":
        entry.active_led_5 = "True"
        db.session.commit()
        return
    if entry.active_led_6 != "True":
        entry.active_led_6 = "True"
        db.session.commit()
        return
    if entry.active_led_7 != "True":
        entry.active_led_7 = "True"
        db.session.commit()
        return
    if entry.active_led_8 != "True":
        entry.active_led_8 = "True"
        db.session.commit()
        return       
    if entry.active_led_9 != "True":
        entry.active_led_9 = "True"
        db.session.commit()
        return  


def REMOVE_LED_GROUP_LED(id):
    entry = LED_Groups.query.filter_by(id=id).first()

    if entry.active_led_9 == "True":
        entry.active_led_9      = "None"
        entry.led_ieeeAddr_9    = "None"
        entry.led_name_9        = "None"
        entry.led_device_type_9 = "None"
        db.session.commit()
        return 

    if entry.active_led_8 == "True":
        entry.active_led_8      = "None"
        entry.led_ieeeAddr_8    = "None"
        entry.led_name_8        = "None"
        entry.led_device_type_8 = "None"
        db.session.commit()  
        return 
    
    if entry.active_led_7 == "True":
        entry.active_led_7      = "None"
        entry.led_ieeeAddr_7    = "None"
        entry.led_name_7        = "None"
        entry.led_device_type_7 = "None"
        db.session.commit()
        return 

    if entry.active_led_6 == "True":
        entry.active_led_6      = "None"
        entry.led_ieeeAddr_6    = "None"
        entry.led_name_6        = "None"
        entry.led_device_type_6 = "None"
        db.session.commit()
        return
    
    if entry.active_led_5 == "True":
        entry.active_led_5      = "None"
        entry.led_ieeeAddr_5    = "None"
        entry.led_name_5        = "None"
        entry.led_device_type_5 = "None"
        db.session.commit()
        return     

    if entry.active_led_4 == "True":
        entry.active_led_4      = "None"
        entry.led_ieeeAddr_4    = "None"
        entry.led_name_4        = "None"
        entry.led_device_type_4 = "None"
        db.session.commit()
        return 

    if entry.active_led_3 == "True":
        entry.active_led_3      = "None"
        entry.led_ieeeAddr_3    = "None"
        entry.led_name_3        = "None"
        entry.led_device_type_3 = "None"
        db.session.commit()
        return     

    if entry.active_led_2 == "True":
        entry.active_led_2      = "None"
        entry.led_ieeeAddr_2    = "None"
        entry.led_name_2        = "None"
        entry.led_device_type_2 = "None"
        db.session.commit()
        return 


def CHANGE_LED_GROUP_POSITION(id, direction):
    
    if direction == "up":
        groups_list = GET_ALL_LED_GROUPS()
        groups_list = groups_list[::-1]
        
        for group in groups_list:
            
            if group.id < id: 
                new_id = group.id
                
                # change ids
                group_1 = GET_LED_GROUP_BY_ID(id)
                group_2 = GET_LED_GROUP_BY_ID(new_id)
                
                group_1.id = 99
                db.session.commit()
                
                group_2.id = id
                group_1.id = new_id
                db.session.commit()
                
                return 

    if direction == "down":
        for group in GET_ALL_LED_GROUPS():
            if group.id > id:
                new_id = group.id
                
                # change ids
                group_1 = GET_LED_GROUP_BY_ID(id)
                group_2 = GET_LED_GROUP_BY_ID(new_id)
                
                group_1.id = 99
                db.session.commit()
                
                group_2.id = id
                group_1.id = new_id
                db.session.commit()
                
                return 


def DELETE_LED_GROUP(id):
    name = GET_LED_GROUP_BY_ID(id).name
    
    try:
        WRITE_LOGFILE_SYSTEM("DATABASE", "LED | Group - " + name + " | deleted")   
    except:
        pass     
    
    LED_Groups.query.filter_by(id=id).delete()
    db.session.commit() 

    return True


""" ################### """
""" ################### """
"""    led scenes     """
""" ################### """
""" ################### """


def GET_ALL_LED_SCENES():
    return LED_Scenes.query.all()   


def GET_LED_SCENE_BY_ID(id):
    return LED_Scenes.query.filter_by(id=id).first()


def GET_LED_SCENE_BY_NAME(name):
    for scene in LED_Scenes.query.all():
        
        if scene.name.lower() == name.lower():
            return scene    
            

def ADD_LED_SCENE(name):

    # find a unused id
    for i in range(1,21):
        if LED_Scenes.query.filter_by(id=i).first():
            pass
        else:
            # add the new program
            scene = LED_Scenes(
                    id = i,
                    name = name,
                )
            db.session.add(scene)
            db.session.commit()

            RESET_LED_SCENE_ERRORS()

            WRITE_LOGFILE_SYSTEM("DATABASE", "LED | Scene - " + name + " | added")  

            return True

    return "Szenenlimit erreicht (20)"


def SET_LED_SCENE(id, name, hex_1, color_temp_1, brightness_1,
                            red_2, green_2, blue_2, color_temp_2, brightness_2,
                            red_3, green_3, blue_3, color_temp_3, brightness_3,
                            red_4, green_4, blue_4, color_temp_4, brightness_4,
                            red_5, green_5, blue_5, color_temp_5, brightness_5,
                            red_6, green_6, blue_6, color_temp_6, brightness_6,
                            red_7, green_7, blue_7, color_temp_7, brightness_7,
                            red_8, green_8, blue_8, color_temp_8, brightness_8,
                            red_9, green_9, blue_9, color_temp_9, brightness_9):

    entry = LED_Scenes.query.filter_by(id=id).first()

    if (entry.name != name or 
        entry.hex_1 != hex_1 or entry.color_temp_1 != int(color_temp_1) or entry.brightness_1 != int(brightness_1) or
        entry.red_2 != int(red_2) or entry.green_2 != int(green_2) or entry.blue_2 != int(blue_2) or entry.color_temp_2 != int(color_temp_2) or entry.brightness_2 != int(brightness_2) or
        entry.red_3 != int(red_3) or entry.green_3 != int(green_3) or entry.blue_3 != int(blue_3) or entry.color_temp_3 != int(color_temp_3) or entry.brightness_3 != int(brightness_3) or
        entry.red_4 != int(red_4) or entry.green_4 != int(green_4) or entry.blue_4 != int(blue_4) or entry.color_temp_4 != int(color_temp_4) or entry.brightness_4 != int(brightness_4) or
        entry.red_5 != int(red_5) or entry.green_5 != int(green_5) or entry.blue_5 != int(blue_5) or entry.color_temp_5 != int(color_temp_5) or entry.brightness_5 != int(brightness_5) or
        entry.red_6 != int(red_6) or entry.green_6 != int(green_6) or entry.blue_6 != int(blue_6) or entry.color_temp_6 != int(color_temp_6) or entry.brightness_6 != int(brightness_6) or
        entry.red_7 != int(red_7) or entry.green_7 != int(green_7) or entry.blue_7 != int(blue_7) or entry.color_temp_7 != int(color_temp_7) or entry.brightness_7 != int(brightness_7) or
        entry.red_8 != int(red_8) or entry.green_8 != int(green_8) or entry.blue_8 != int(blue_8) or entry.color_temp_8 != int(color_temp_8) or entry.brightness_8 != int(brightness_8) or
        entry.red_9 != int(red_9) or entry.green_9 != int(green_9) or entry.blue_9 != int(blue_9) or entry.color_temp_9 != int(color_temp_9) or entry.brightness_9 != int(brightness_9)):

        entry.name  = name
        entry.hex_1 = hex_1
        entry.color_temp_1 = color_temp_1
        entry.brightness_1 = brightness_1
        entry.red_2 = red_2
        entry.green_2 = green_2   
        entry.blue_2 = blue_2
        entry.color_temp_2 = color_temp_2
        entry.brightness_2 = brightness_2
        entry.red_3 = red_3
        entry.green_3 = green_3   
        entry.blue_3 = blue_3
        entry.color_temp_3 = color_temp_3
        entry.brightness_3 = brightness_3    
        entry.red_4 = red_4
        entry.green_4 = green_4   
        entry.blue_4 = blue_4
        entry.color_temp_4 = color_temp_4
        entry.brightness_4 = brightness_4
        entry.red_5 = red_5
        entry.green_5 = green_5   
        entry.blue_5 = blue_5
        entry.color_temp_5 = color_temp_5
        entry.brightness_5 = brightness_5
        entry.red_6 = red_6
        entry.green_6 = green_6   
        entry.blue_6 = blue_6
        entry.color_temp_6 = color_temp_6
        entry.brightness_6 = brightness_6
        entry.red_7 = red_7
        entry.green_7 = green_7   
        entry.blue_7 = blue_7
        entry.color_temp_7 = color_temp_7
        entry.brightness_7 = brightness_7
        entry.red_8 = red_8
        entry.green_8 = green_8   
        entry.blue_8 = blue_8
        entry.color_temp_8 = color_temp_8
        entry.brightness_8 = brightness_8
        entry.red_9 = red_9
        entry.green_9 = green_9   
        entry.blue_9 = blue_9
        entry.color_temp_9 = color_temp_9
        entry.brightness_9 = brightness_9                    
        db.session.commit()  

        WRITE_LOGFILE_SYSTEM("DATABASE", "LED | Scene - " + name + " | Settings changed") 

        return True


def ADD_LED_SCENE_SETTING(id):
    entry = LED_Scenes.query.filter_by(id=id).first()

    if entry.active_setting_2 != "True":
        entry.active_setting_2 = "True"   
        db.session.commit()
        return
    if entry.active_setting_3 != "True":
        entry.active_setting_3 = "True"      
        db.session.commit()
        return
    if entry.active_setting_4 != "True":
        entry.active_setting_4 = "True"   
        db.session.commit()
        return
    if entry.active_setting_5 != "True":
        entry.active_setting_5 = "True"  
        db.session.commit()
        return
    if entry.active_setting_6 != "True":
        entry.active_setting_6 = "True"   
        db.session.commit()
        return
    if entry.active_setting_7 != "True":
        entry.active_setting_7 = "True"  
        db.session.commit()
        return
    if entry.active_setting_8 != "True":
        entry.active_setting_8 = "True"     
        db.session.commit()
        return       
    if entry.active_setting_9 != "True":
        entry.active_setting_9 = "True"
        entry.brightness_9     = 254
        db.session.commit()
        return  


def REMOVE_LED_SCENE_SETTING(id):
    entry = LED_Scenes.query.filter_by(id=id).first()

    if entry.active_setting_9 == "True":
        entry.active_setting_9 = "None"
        entry.red_9            = 0
        entry.green_9          = 0
        entry.blue_9           = 0
        entry.color_temp_9     = 0
        entry.brightness_9     = 254
        db.session.commit()
        return

    if entry.active_setting_8 == "True":
        entry.active_setting_8 = "None"
        entry.red_8            = 0
        entry.green_8          = 0
        entry.blue_8           = 0
        entry.color_temp_8     = 0
        entry.brightness_8     = 254
        db.session.commit()
        return

    if entry.active_setting_7 == "True":
        entry.active_setting_7 = "None"
        entry.red_7            = 0
        entry.green_7          = 0
        entry.blue_7           = 0
        entry.color_temp_7     = 0
        entry.brightness_7     = 254
        db.session.commit()
        return

    if entry.active_setting_6 == "True":
        entry.active_setting_6 = "None"
        entry.red_6            = 0
        entry.green_6          = 0
        entry.blue_6           = 0
        entry.color_temp_6     = 0
        entry.brightness_6     = 254
        db.session.commit()
        return

    if entry.active_setting_5 == "True":
        entry.active_setting_5 = "None"
        entry.red_5            = 0
        entry.green_5          = 0
        entry.blue_5           = 0
        entry.color_temp_5     = 0
        entry.brightness_5     = 254
        db.session.commit()
        return

    if entry.active_setting_4 == "True":
        entry.active_setting_4 = "None"
        entry.red_4            = 0
        entry.green_4          = 0
        entry.blue_4           = 0
        entry.color_temp_4     = 0
        entry.brightness_4     = 254
        db.session.commit()
        return

    if entry.active_setting_3 == "True":
        entry.active_setting_3 = "None"
        entry.red_3            = 0
        entry.green_3          = 0
        entry.blue_3           = 0
        entry.color_temp_3     = 0
        entry.brightness_3     = 254
        db.session.commit()
        return

    if entry.active_setting_2 == "True":
        entry.active_setting_2 = "None"
        entry.red_2            = 0
        entry.green_2          = 0
        entry.blue_2           = 0
        entry.color_temp_2     = 0
        entry.brightness_2     = 254
        db.session.commit()
        return


def SET_LED_SCENE_COLLAPSE_OPEN(id):
    list_led_scenes = LED_Scenes.query.all()
    
    for led_scene in list_led_scenes:
        led_scene.collapse = ""
        db.session.commit()   
  
    entry = LED_Scenes.query.filter_by(id=id).first()
    
    entry.collapse = "True"
    db.session.commit()   


def RESET_LED_SCENE_COLLAPSE():
    list_led_scenes = LED_Scenes.query.all()
    
    for led_scene in list_led_scenes:
        led_scene.collapse = ""
        db.session.commit()   


def CHANGE_LED_SCENES_POSITION(id, direction):
    
    if direction == "up":
        scenes_list = GET_ALL_LED_SCENES()
        scenes_list = scenes_list[::-1]
        
        for scene in scenes_list:
            
            if scene.id < id:    
                new_id = scene.id
                
                # change ids
                scene_1 = GET_LED_SCENE_BY_ID(id)
                scene_2 = GET_LED_SCENE_BY_ID(new_id)
                
                scene_1.id = 99
                db.session.commit()
                
                scene_2.id = id
                scene_1.id = new_id
                db.session.commit()
                
                return 

    if direction == "down":
        for scene in GET_ALL_LED_SCENES():
            if scene.id > id:   
                new_id = scene.id
                
                # change ids
                scene_1 = GET_LED_SCENE_BY_ID(id)
                scene_2 = GET_LED_SCENE_BY_ID(new_id)
                
                scene_1.id = 99
                db.session.commit()
                
                scene_2.id = id
                scene_1.id = new_id
                db.session.commit()
                
                return 


def DELETE_LED_SCENE(id):
    name = GET_LED_SCENE_BY_ID(id).name
    
    try:
        WRITE_LOGFILE_SYSTEM("DATABASE", "LED | Scene - " + name + " | deleted") 
    except:
        pass 

    LED_Scenes.query.filter_by(id=id).delete()
    db.session.commit() 

    return True


""" ################### """
""" ################### """
"""     mqtt broker     """
""" ################### """
""" ################### """


def GET_MQTT_BROKER_SETTINGS():
    return MQTT_Broker.query.filter_by().first()


def SET_MQTT_BROKER_SETTINGS(broker, user, password):
    entry = MQTT_Broker.query.filter_by().first()

    if (entry.broker != broker or entry.user != user or entry.password != password):
 
        entry.previous_broker   = entry.broker
        entry.previous_user     = entry.user
        entry.previous_password = entry.password
        entry.broker            = broker
        entry.user              = user
        entry.password          = password

        db.session.commit()  
    
        WRITE_LOGFILE_SYSTEM("DATABASE", "MQTT | Broker Settings changed")

        return True


def RESTORE_MQTT_BROKER_SETTINGS():
    entry = MQTT_Broker.query.filter_by().first()

    broker                  = entry.broker
    user                    = entry.user
    password                = entry.password

    entry.broker            = entry.previous_broker
    entry.user              = entry.previous_user
    entry.password          = entry.previous_password
    entry.previous_broker   = broker
    entry.previous_user     = user
    entry.previous_password = password

    db.session.commit()

    WRITE_LOGFILE_SYSTEM("DATABASE", "MQTT | Broker Settings restored")


""" ################### """
""" ################### """
"""       plants        """
""" ################### """
""" ################### """


def GET_PLANT_BY_ID(id):
    return Plants.query.filter_by(id=id).first()


def GET_PLANT_BY_NAME(name):
    for plant in Plants.query.all():
        
        if plant.name.lower() == name.lower():
            return plant    
    

def GET_PLANT_BY_IEEEADDR(device_ieeeAddr):
    return Plants.query.filter_by(device_ieeeAddr=device_ieeeAddr).first()


def GET_ALL_PLANTS():
    return Plants.query.all()


def ADD_PLANT(name, device_ieeeAddr):
    # name exist ?
    if not GET_PLANT_BY_NAME(name):
        
        # find a unused id
        for i in range(1,26):
            if Plants.query.filter_by(id=i).first():
                pass
            else:
                # add the new plant
                plant = Plants(
                        id                     = i,
                        name                   = name, 
                        device_ieeeAddr        = device_ieeeAddr,     
                        group                  = 1,
                        pump_duration_auto     = 0, 
                        pump_duration_manually = 30,                                               
                    )
                db.session.add(plant)
                db.session.commit()

                WRITE_LOGFILE_SYSTEM("DATABASE", "Plant - " + name + " | added")  

                # create data_file
                CREATE_PLANTS_DATAFILE(name)
                return
  
                          
        return "Plantslimit reached (25)"

    else:
        return "Name already assigned"


def UPDATE_PLANT_SETTINGS(id, name, group):         
    entry = Plants.query.filter_by(id=id).first()
    old_name = entry.name

    # values changed ?
    if (entry.name != name or entry.group != int(group)):

        entry.name  = name
        entry.group = group        
        
        db.session.commit()  
        
        WRITE_LOGFILE_SYSTEM("DATABASE", "Plant - " + old_name + " | changed || Name - " + entry.name + " | Group - " + str(entry.group))

        # rename data_file
        if old_name != name:
            RENAME_PLANTS_DATAFILE(old_name, name)

        return True


def SET_PLANT_MOISTURE_LEVEL(id, moisture_level):         
    entry = Plants.query.filter_by(id=id).first()

    # values changed ?
    if entry.moisture_level != moisture_level: 

        entry.moisture_level = moisture_level
        db.session.commit()  
        
        if entry.moisture_level != "None":
            WRITE_LOGFILE_SYSTEM("DATABASE", "Plant - " + entry.name + " | changed || Moisture_Level - " + str(entry.moisture_level))   

        return True 

    
def SET_PLANT_PUMP_DURATION_AUTO(id, pump_duration_auto):         
    entry = Plants.query.filter_by(id=id).first()

    # values changed ?
    if entry.pump_duration_auto != int(pump_duration_auto):      

        entry.pump_duration_auto = pump_duration_auto
        db.session.commit()  
        
        if entry.pump_duration_auto != "None":
            WRITE_LOGFILE_SYSTEM("DATABASE", "Plant - " + entry.name + " | changed || Pump_Duration_Auto - " + str(entry.pump_duration_auto)) 

        return True    


def SET_PLANT_PUMP_DURATION_MANUALLY(id, pump_duration_manually):         
    entry = Plants.query.filter_by(id=id).first()

    # values changed ?
    if entry.pump_duration_manually != int(pump_duration_manually):       

        entry.pump_duration_manually = pump_duration_manually
        db.session.commit()  
        
        if entry.pump_duration_manually != "None":
            WRITE_LOGFILE_SYSTEM("DATABASE", "Plant - " + entry.name + " | changed || Pump_Duration_Manually - " + str(entry.pump_duration_manually))   

        return True                               


def CHANGE_PLANTS_POSITION(id, direction):
    
    if direction == "up":
        plants_list = GET_ALL_PLANTS()
        plants_list = plants_list[::-1]
        
        for plant in plants_list:
            
            if plant.id < id:     
                new_id = plant.id
                
                # change ids
                plant_1 = GET_PLANT_BY_ID(id)
                plant_2 = GET_PLANT_BY_ID(new_id)
                
                plant_1.id = 99
                db.session.commit()
                
                plant_2.id = id
                plant_1.id = new_id
                db.session.commit()
                
                return 

    if direction == "down":
        for plant in GET_ALL_PLANTS():
            if plant.id > id:       
                new_id = plant.id
                
                # change ids
                plant_1 = GET_PLANT_BY_ID(id)
                plant_2 = GET_PLANT_BY_ID(new_id)
                
                plant_1.id = 99
                db.session.commit()
                
                plant_2.id = id
                plant_1.id = new_id
                db.session.commit()
                
                return 


def DELETE_PLANT(id):
    entry = GET_PLANT_BY_ID(id)
    plant_name = entry.name
    
    try:
        WRITE_LOGFILE_SYSTEM("DATABASE", "Plant - " + plant_name + " | deleted")   
        Plants.query.filter_by(id=id).delete()
        db.session.commit()

        # delete data_file
        DELETE_PLANTS_DATAFILE(plant_name)
        return True

    except Exception as e:
        return(e)


""" ################## """
""" ################## """
"""      scheduler     """
""" ################## """
""" ################## """


def GET_SCHEDULER_TASK_BY_ID(id):
    return Scheduler_Tasks.query.filter_by(id=id).first()


def GET_SCHEDULER_TASK_BY_NAME(name):
    for task in Scheduler_Tasks.query.all():
        
        if task.name.lower() == name.lower():
            return task    
    

def GET_ALL_SCHEDULER_TASKS():
    return Scheduler_Tasks.query.all()    


def UPDATE_SCHEDULER_TASK(id, hour, minute, pause): 
    entry = Scheduler_Tasks.query.filter_by(id=id).first()

    # values changed ?
    if (entry.hour != int(hour) or entry.minute != int(minute) or entry.pause != pause):
            
        entry.hour   = hour
        entry.minute = minute        
        entry.pause  = pause      

        db.session.commit()   

        WRITE_LOGFILE_SYSTEM("DATABASE", "Task - " + entry.name + " | changed " +
                             "|| Time - " + str(entry.hour) + ":" + str(entry.minute) + 
                             " | Pause - " + str(entry.pause))     

        return True


""" ################### """
""" ################### """
"""   user management   """
""" ################### """
""" ################### """


def GET_USER_BY_ID(id):
    return User.query.get(int(id))


def GET_USER_BY_NAME(username):
    for user in User.query.all():
        
        if user.username.lower() == username.lower():
            return user       
 

def GET_USER_BY_EMAIL(email):
    return User.query.filter_by(email=email).first()  


def GET_ALL_USERS():
    return User.query.all()  
    

def ADD_USER(username, email, password):
    # username exist ?
    if not GET_USER_BY_NAME(username):

        # email exist ?
        if not GET_USER_BY_EMAIL(email):
        
            # add the new user
            new_user = User(
                    username           = username,
                    email              = email,
                    password           = password,
                    role               = "user",
                    email_notification = "False",
                )
            db.session.add(new_user)
            db.session.commit()

            WRITE_LOGFILE_SYSTEM("DATABASE", "User - " + username + " | added") 

            return 

        else:
            return "eMail-Address already assigned"               

    else:
        return "Name already assigned"    


def UPDATE_USER_SETTINGS(id, username, email, role, email_notification):    
    
    entry = User.query.filter_by(id=id).first()
    old_username = entry.username

    # values changed ?
    if (entry.username != username or entry.email != email or entry.role != role or entry.email_notification != email_notification):

        entry.username           = username
        entry.email              = email
        entry.role               = role 
        entry.email_notification = email_notification
        db.session.commit()
        
        WRITE_LOGFILE_SYSTEM("DATABASE", "User - " + old_username + " | changed || Username - " + entry.username +
                             " | eMail - " + entry.email + " | Role - " + entry.role + " | eMail-Notification - " + entry.email_notification)

        return True


def CHANGE_USER_PASSWORD(id, hashed_password):
    entry = User.query.filter_by(id=id).first()

    # values changed ?
    if entry.password != hashed_password:    
    
        entry.password = hashed_password    
        db.session.commit()
        
        WRITE_LOGFILE_SYSTEM("DATABASE", "User - " + entry.username + " | Password changed")

        return True
    

def DELETE_USER(user_id):
    entry = GET_USER_BY_ID(user_id)

    try:
        WRITE_LOGFILE_SYSTEM("DATABASE", "User - " + entry.username + " | deleted")    
        User.query.filter_by(id=user_id).delete()
        db.session.commit()    
        return True

    except Exception as e:
        return(e)


""" ################### """
""" ################### """
"""     zigbee2mqtt     """
""" ################### """
""" ################### """

    
def GET_ZIGBEE2MQTT_PAIRING():
    return ZigBee2MQTT.query.filter_by().first().pairing


def SET_ZIGBEE2MQTT_PAIRING(setting):
    entry = ZigBee2MQTT.query.filter_by().first()
    entry.pairing = setting
    db.session.commit()