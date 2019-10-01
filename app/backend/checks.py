from app                         import app
from app.database.models         import *

import datetime


""" ################### """
"""  device exceptions  """
""" ################### """

def CHECK_DEVICE_EXCEPTION_SETTINGS(devices): 
   error_message_settings = []

   for device in devices:

      if device.exception_option != "None":

         if device.exception_setting == "None" or device.exception_setting == None:
            error_message_settings.append(device.name + " || Keine Aufgabe ausgewählt")         

         # exception setting ip_address
         if device.exception_option == "IP-Address":

            # search for wrong chars
            for element in device.exception_value_1:
               if not element.isdigit() and element != "." and element != "," and element != " ":
                  error_message_settings.append(device.name + " || Ungültige IP-Adresse")
                  break
               
         # exception setting sensor
         if device.exception_option != "IP-Address": 
            
            if device.exception_value_1 == "None" or device.exception_value_1 == None:
               error_message_settings.append(device.name + " || Keinen Sensor ausgewählt")

            if device.exception_value_2 == "None" or device.exception_value_2 == None:
               error_message_settings.append(device.name + " || Keinen Operator (<, >, =) eingetragen")

            if device.exception_value_3 == "None" or device.exception_value_3 == None:
               error_message_settings.append(device.name + " || Keinen Vergleichswert eingetragen")
                  
   return error_message_settings


""" ################## """
"""  check led groups  """
""" ################## """

def CHECK_LED_GROUP_SETTINGS(settings):
   list_errors = []

   # check setting open led_slots in groups
   for element in settings:
      
      if element.led_ieeeAddr_1 == None or element.led_ieeeAddr_1 == "None":
          list_errors.append(element.name + " >>> fehlende Einstellung >>> LED 1")        
      if element.active_led_2 == "True" and (element.led_ieeeAddr_2 == None or element.led_ieeeAddr_2 == "None"):
          list_errors.append(element.name + " >>> fehlende Einstellung >>> LED 2") 
      if element.active_led_3 == "True" and (element.led_ieeeAddr_3 == None or element.led_ieeeAddr_3 == "None"):
          list_errors.append(element.name + " >>> fehlende Einstellung >>> LED 3") 
      if element.active_led_4 == "True" and (element.led_ieeeAddr_4 == None or element.led_ieeeAddr_4 == "None"):
          list_errors.append(element.name + " >>> fehlende Einstellung >>> LED 4") 
      if element.active_led_5 == "True" and (element.led_ieeeAddr_5 == None or element.led_ieeeAddr_5 == "None"):
          list_errors.append(element.name + " >>> fehlende Einstellung >>> LED 5") 
      if element.active_led_6 == "True" and (element.led_ieeeAddr_6 == None or element.led_ieeeAddr_6 == "None"):
          list_errors.append(element.name + " >>> fehlende Einstellung >>> LED 6") 
      if element.active_led_7 == "True" and (element.led_ieeeAddr_7 == None or element.led_ieeeAddr_7 == "None"):
          list_errors.append(element.name + " >>> fehlende Einstellung >>> LED 7") 
      if element.active_led_8 == "True" and (element.led_ieeeAddr_8 == None or element.led_ieeeAddr_8 == "None"):
          list_errors.append(element.name + " >>> fehlende Einstellung >>> LED 8") 
      if element.active_led_9 == "True" and (element.led_ieeeAddr_9 == None or element.led_ieeeAddr_9 == "None"):
          list_errors.append(element.name + " >>> fehlende Einstellung >>> LED 9")   
          
   return list_errors


""" ################### """
"""     check tasks     """
""" ################### """

def CHECK_TASKS(tasks, task_type):
   list_task_errors = []


   if task_type == "scheduler": 

      for element in tasks:

         result = CHECK_TASK_OPERATION(element.task, element.name, task_type)
         
         if result != []:
            
            for error in result:   
               list_task_errors.append(error)
               

   if task_type == "controller": 

      for controller in tasks:

         name = GET_DEVICE_BY_IEEEADDR(controller.device_ieeeAddr).name

         if controller.command_1 != None and controller.command_1 != "None": 
            result = CHECK_TASK_OPERATION(controller.task_1, name, task_type, controller.command_1)
            
            if result != []:
               
               for error in result:   
                  list_task_errors.append(error)    
               
         if controller.command_2 != None and controller.command_2 != "None": 
            result = CHECK_TASK_OPERATION(controller.task_2, name, task_type, controller.command_2)
            
            if result != []:
               
               for error in result:   
                  list_task_errors.append(error)        
                         
         if controller.command_3 != None and controller.command_3 != "None": 
            result = CHECK_TASK_OPERATION(controller.task_3, name, task_type, controller.command_3)
            
            if result != []:
               
               for error in result:   
                  list_task_errors.append(error)                 
               
         if controller.command_4 != None and controller.command_4 != "None": 
            result = CHECK_TASK_OPERATION(controller.task_4, name, task_type, controller.command_4)
            
            if result != []:
               
               for error in result:   
                  list_task_errors.append(error)       
               
         if controller.command_5 != None and controller.command_5 != "None": 
            result = CHECK_TASK_OPERATION(controller.task_5, name, task_type, controller.command_5)
            
            if result != []:
               
               for error in result:   
                  list_task_errors.append(error)                     
               
         if controller.command_6 != None and controller.command_6 != "None": 
            result = CHECK_TASK_OPERATION(controller.task_6, name, task_type, controller.command_6)
            
            if result != []:
               
               for error in result:   
                  list_task_errors.append(error)       
               
         if controller.command_7 != None and controller.command_7 != "None": 
            result = CHECK_TASK_OPERATION(controller.task_7, name, task_type, controller.command_7)
            
            if result != []:
               
               for error in result:   
                  list_task_errors.append(error)                   
               
         if controller.command_8 != None and controller.command_8 != "None": 
            result = CHECK_TASK_OPERATION(controller.task_8, name, task_type, controller.command_8)
            
            if result != []:
               
               for error in result:   
                  list_task_errors.append(error)                   
                                             
         if controller.command_9 != None and controller.command_9 != "None": 
            result = CHECK_TASK_OPERATION(controller.task_9, name, task_type, controller.command_9)
            
            if result != []:
               
               for error in result:   
                  list_task_errors.append(error)             
    
   return list_task_errors


def CHECK_TASK_OPERATION(task, name, task_type, controller_command = ""):
   
   list_task_errors   = []
   controller_command = controller_command[1:-1].replace('"','')

   try:
      
      # #############
      #  start_scene
      # #############
      
      if "scene" in task:
         if " /// " in task:
            task = task.split(" /// ") 

            # check group setting 
            try:
               group_exist = False

               input_group_name = task[1]
               input_group_name = input_group_name.lower()

               # get exist group names and lower the letters
               all_exist_groups = GET_ALL_LED_GROUPS()
               
               for exist_group in all_exist_groups:
                  
                  exist_group_name       = exist_group.name
                  exist_group_name_lower = exist_group_name.lower()
                  
                  # compare the formated names
                  if input_group_name == exist_group_name_lower: 
                     group_exist = True
                     
               if group_exist == True:
                  pass
                  
               else:
                  if task_type == "controller":
                     list_task_errors.append(name + " >>> " + controller_command + " >>> LED Gruppe nicht vorhanden >>> " + task[1])
                  else:
                     list_task_errors.append(name + " >>> LED Gruppe nicht vorhanden >>> " + task[1])

            except:
               if task_type == "controller":
                  list_task_errors.append(name + " >>> " + controller_command + " >>> fehlende Einstellung >>> LED Gruppe")
               else:
                  list_task_errors.append(name + " >>> fehlende Einstellung >>> LED Gruppe")

            # check scene setting    
            try:
               scene_exist = False

               input_scene_name = task[2]
               input_scene_name = input_scene_name.lower()

               # get exist scene names and lower the letters
               all_exist_scenes = GET_ALL_LED_SCENES()
               
               for exist_scene in all_exist_scenes:
                  
                  exist_scene_name       = exist_scene.name
                  exist_scene_name_lower = exist_scene_name.lower()
                  
                  # compare the formated names
                  if input_scene_name == exist_scene_name_lower: 
                     scene_exist = True
                     
               if scene_exist == True:
                  pass
                  
               else:
                  if task_type == "controller":
                     list_task_errors.append(name + " >>> " + controller_command + " >>> LED Szene nicht vorhanden >>> " + task[2])
                  else:                  
                     list_task_errors.append(name + " >>> LED Szene nicht vorhanden >>> " + task[2])

            except:
               if task_type == "controller":
                  list_task_errors.append(name + " >>> " + controller_command + " >>> fehlende Einstellung >>> LED Szene")
               else:               
                  list_task_errors.append(name + " >>> fehlende Einstellung >>> LED Szene")

            # check global brightness    
            try:
               if task[3].isdigit():
                  if 1 <= int(task[3]) <= 100:
                     return list_task_errors

                  else:
                     if task_type == "controller":
                        list_task_errors.append(name + " >>> " + controller_command + " >>> ungültiger Wertebereich >>> Globale Helligkeit")
                     else:                        
                        list_task_errors.append(name + " >>> ungültiger Wertebereich >>> Globale Helligkeit") 
                     return list_task_errors    

               else:
                  if task_type == "controller":
                     list_task_errors.append(name + " >>> " + controller_command + " >>> ungültige Einstellung >>> Globale Helligkeit")
                  else:                     
                     list_task_errors.append(name + " >>> ungültige Einstellung >>> Globale Helligkeit")
                  return list_task_errors

            except:
               return list_task_errors

         else:
            if task_type == "controller":
               list_task_errors.append(name + " >>> " + controller_command + " >>> Ungültige Formatierung")
            else:                
               list_task_errors.append(name + " >>> Ungültige Formatierung")
            return list_task_errors
     
     
      # ###################
      #  brightness dimmer
      # ###################
      
      
      if "brightness" in task and task_type == "controller":
         if " /// " in task:
            task = task.split(" /// ") 

            # check group setting
            try:
               if GET_LED_GROUP_BY_NAME(task[1]):
                  pass
                  
               else:
                  list_task_errors.append(name + " >>> " + controller_command + " >>> LED Gruppe nicht vorhanden >>> " + task[1])   
                                    
            except:
               list_task_errors.append(name + " >>> " + controller_command + " >>> fehlende Einstellung >>> LED Gruppe")      

            # check brightness setting    
            try:
               if task[2] == "turn_up" or task[2] == "TURN_UP" or task[2] == "turn_down" or task[2] == "TURN_DOWN":
                  return list_task_errors
                  
               else:
                  list_task_errors.append(name + " >>> " + controller_command + " >>> TURN_UP oder TURN_DOWN ?")
                  return list_task_errors
                  
            except:
               list_task_errors.append(name + " >>> " + controller_command + " >>> fehlende Einstellung >>> TURN_UP oder TURN_DOWN")    
               return list_task_errors

         else:
            list_task_errors.append(name + " >>> " + controller_command + " >>> Ungültige Formatierung")
            return list_task_errors


      # #########
      #  led_off
      # #########
      
      
      if "led_off" in task:
         if " /// " in task:
            task = task.split(" /// ")
            
            # check group setting
            if "group" in task[1]:

               try:
                  
                  # get input group names and lower the letters
                  try:
                        list_groups = task[2].split(",")
                  except:
                        list_groups = [task[2]]

                  for input_group_name in list_groups:
                        
                     input_group_name = input_group_name.replace(" ", "")
                     input_group_name = input_group_name.lower()

                     # get exist group names and lower the letters
                     try:
                        all_exist_group = GET_ALL_LED_GROUPS()
                        
                        group_exist = False
                        
                        for exist_group in all_exist_group:
                           
                           exist_group_name = exist_group.name
                           exist_group_name = exist_group_name.lower()
                           
                           # compare the formated names
                           if input_group_name == exist_group_name: 
                              group_exist = True
                           
                        if group_exist == True:
                           pass
                           
                        else:
                           if task_type == "controller":
                              list_task_errors.append(name + " >>> " + controller_command + " >>> LED Gruppe nicht vorhanden >>> " + input_group_name)  
                           else:                               
                              list_task_errors.append(name + " >>> LED Gruppe nicht vorhanden >>> " + input_group_name)  
                        
                        return list_task_errors
                        
                     except:
                        if task_type == "controller":
                           list_task_errors.append(name + " >>> " + controller_command + " >>> fehlende Einstellung >>> LED Gruppe")
                        else:                            
                           list_task_errors.append(name + " >>> fehlende Einstellung >>> LED Gruppe")
                        
                        return list_task_errors
                        
               except:
                  if task_type == "controller":
                     list_task_errors.append(name + " >>> " + controller_command + " >>> fehlende Einstellung >>> LED Gruppe")
                  else:                            
                     list_task_errors.append(name + " >>> fehlende Einstellung >>> LED Gruppe")
                  
                  return list_task_errors 

               
            # check turn off all leds
            elif task[1] == "all" or task[1] == "ALL": 
               return list_task_errors


            else:
               if task_type == "controller":
                  list_task_errors.append(name + " >>> " + controller_command + " >>> Ungültige Eingabe >>> 'all' oder 'group'")
               else:                   
                  list_task_errors.append(name + " >>> Ungültige Eingabe >>> 'all' oder 'group' ?")
               return list_task_errors  


         else:
            if task_type == "controller":
               list_task_errors.append(name + " >>> " + controller_command + " >>> Ungültige Formatierung") 
            else:                   
               list_task_errors.append(name + " >>> Ungültige Formatierung")     
            return list_task_errors


      # ########
      #  device
      # ########
      
      
      if "device" in task and "update" not in task:
         if " /// " in task:
            task = task.split(" /// ") 

            try:
               device  = GET_DEVICE_BY_NAME(task[1].lower())
               
               setting_formated = task[2]
               setting_formated = setting_formated.replace(" ", "")

               # convert string to json-format
               setting = setting_formated.replace(':', '":"')
               setting = setting.replace(',', '","')
               setting = '{"' + str(setting) + '"}'    

               setting_valid = False

               # check device command 
               for command in device.commands.split(" "):   
                  if command == setting:
                     setting_valid = True
                     break

               if setting_valid == False:

                  if task_type == "controller":
                     list_task_errors.append(name + " >>> " + controller_command + " >>> Ungültiger Befehl >>> " + task[2])
                  else:
                     list_task_errors.append(name + " >>> Ungültiger Befehl >>> " + task[2])
                             
               return list_task_errors                  
              
            except:
               
               if task_type == "controller":
                  list_task_errors.append(name + " >>> " + controller_command + " >>> Gerät nicht gefunden >>> " + task[1])
               else:
                  list_task_errors.append(name + " >>> Gerät nicht gefunden >>> " + task[1])
                  
               return list_task_errors

         else:
            if task_type == "controller":
               list_task_errors.append(name + " >>> " + controller_command + " >>> Ungültige Formatierung")
            else:                
               list_task_errors.append(name + " >>> Ungültige Formatierung")       
            return list_task_errors
            

      # #########
      #  program
      # #########
      
      
      if "program" in task:
         if " /// " in task:
            task = task.split(" /// ") 

            try:
               program = GET_PROGRAM_BY_NAME(task[1].lower())
               setting = task[2].lower()
                  
               if program == None:
               
                  if task_type == "controller":
                     list_task_errors.append(name + " >>> " + controller_command + " >>> Programm nicht gefunden >>> " + task[1])
                  else:
                     list_task_errors.append(name + " >>> " + task[1] + " Programm nicht gefunden")                  
                  
               if setting != "start" and setting != "stop":
                  
                  if task_type == "controller":
                     list_task_errors.append(name + " >>> " + controller_command + " >>> Ungültiger Befehl >>> " + task[2])
                  else:
                     list_task_errors.append(name + " >>> Ungültiger Befehl >>> " + task[2])
               
               return list_task_errors
      
      
            except:
               if task_type == "controller":
                  list_task_errors.append(name + " >>> " + controller_command + " >>> Ungültige Formatierung")
               else:
                  list_task_errors.append(name + " >>> Ungültige Formatierung")
               return list_task_errors
         
         
         else:
            if task_type == "controller":
               list_task_errors.append(name + " >>> " + controller_command + " >>> Ungültige Formatierung")
            else:                
               list_task_errors.append(name + " >>> Ungültige Formatierung")
            return list_task_errors
         

      # #################
      #  watering_plants
      # #################
      
      
      if "watering_plants" in task and task_type == "scheduler":
         if " /// " in task:
            task = task.split(" /// ") 
            
            try:
               if task[1] not in ["1", "2", "3", "4", "5"] and task[1] != "all" and task[1] != "ALL":
                  list_task_errors.append(name + " >>> keine gültige Gruppe angegeben")
            except:
               list_task_errors.append(name + " >>> keine gültige Gruppe angegeben")
            
         else:                
            list_task_errors.append(name + " >>> Ungültige Formatierung")
         return list_task_errors
         

      # ###############
      #  save_database  
      # ###############  
      
           
      if task == "save_database" and task_type == "scheduler":
         return list_task_errors


      # ################
      #  update_devices
      # #################
      
      
      if task == "update_devices" and task_type == "scheduler":
         return list_task_errors


      # ####################
      #  request_sensordata
      # ####################
      
      
      if "request_sensordata" in task and task_type == "scheduler":
         if " /// " in task:
            task = task.split(" /// ")

            # check job name setting
            try:          
               if GET_SENSORDATA_JOB_BY_NAME(task[1]):
                  return list_task_errors

               else:
                  list_task_errors.append(name + " >>> Job nicht vorhanden >>> " + task[1])
                  return list_task_errors   

            except:
               list_task_errors.append(name + " >>> fehlende Einstellung >>> Job-Name") 
               return list_task_errors

         else:
            list_task_errors.append(name + " >>> Ungültige Formatierung")
            return list_task_errors


      # #########
      #  spotify     
      # #########
      
         
      if "spotify" in task:
         if " /// " in task:
            task = task.split(" /// ")

            # check settings
            try:   
                   
               if task[1].lower() == "play":
                  return list_task_errors

               elif task[1].lower() == "previous":
                  return list_task_errors
             
               elif task[1].lower() == "next":
                  return list_task_errors   
                  
               elif task[1].lower() == "stop":
                  return list_task_errors
             
               elif task[1].lower() == "turn_up":
                  return list_task_errors                     
                                 
               elif task[1].lower() == "turn_down":
                  return list_task_errors
             
               elif task[1].lower() == "volume":             
             
                  try:
                     if not task[2].isdigit():
                        list_task_errors.append(name + " >>> """ + task[2] + " >>> Ungültiger Lautstärkewert") 
                     else:
                        if not 0 <= int(task[2]) <= 100:
                           list_task_errors.append(name + " >>> """ + task[2] + " >>> Zulässige Lautstärke liegt zwischen 0 % und 100 %")
                           
                     return list_task_errors
                           
                  except:
                     list_task_errors.append(name + " >>> """ + task[2] + " >>> Ungültiger Lautstärkewert") 
                     return list_task_errors
                  
               elif task[1].lower() == "playlist": 
                  
                  try:
                     device_name   = task[2]                                    
                     playlist_name = task[3]
                     
                     try:
                        if not task[4].isdigit():
                           list_task_errors.append(name + " >>> """ + task[4] + " >>> Ungültiger Lautstärkewert") 
                        else:
                           if not 0 <= int(task[4]) <= 100:
                              list_task_errors.append(name + " >>> """ + task[4] + " >>> Zulässige Lautstärke liegt zwischen 0 % und 100 %")
                              
                        return list_task_errors
                                 
                     except:
                        list_task_errors.append(name + " >>> """ + task[4] + " >>> Ungültiger Lautstärkewert") 
                        return list_task_errors
                        
                  except:
                     list_task_errors.append(name + " >>> """ + str(task) + " >>> Unvollständige Angaben")  
                     return list_task_errors                
                     
               elif task[1].lower() == "track": 
                  
                  try:
                     device_name  = task[2]                                    
                     track_title  = task[3]
                     track_artist = task[4]
                     
                     try:
                        if not task[5].isdigit():
                           list_task_errors.append(name + " >>> """ + task[5] + " >>> Ungültiger Lautstärkewert") 
                        else:
                           if not 0 <= int(task[5]) <= 100:
                              list_task_errors.append(name + " >>> """ + task[5] + " >>> Zulässige Lautstärke liegt zwischen 0 % und 100 %")
                              
                        return list_task_errors
                                 
                     except:
                        list_task_errors.append(name + " >>> """ + task[5] + " >>> Ungültiger Lautstärkewert") 
                        return list_task_errors
                        
                  except:
                     list_task_errors.append(name + " >>> """ + str(task) + " >>> Unvollständige Angaben") 
                     return list_task_errors  

               elif task[1].lower() == "album": 
                  
                  try:
                     device_name  = task[2]                                    
                     album_title  = task[3]
                     album_artist = task[4]
                     
                     try:
                        if not task[5].isdigit():
                           list_task_errors.append(name + " >>> """ + task[5] + " >>> Ungültiger Lautstärkewert") 
                        else:
                           if not 0 <= int(task[5]) <= 100:
                              list_task_errors.append(name + " >>> """ + task[5] + " >>> Zulässige Lautstärke liegt zwischen 0 % und 100 %")
                        
                        return list_task_errors
                                 
                     except:
                        list_task_errors.append(name + " >>> """ + task[5] + " >>> Ungültiger Lautstärkewert") 
                        return list_task_errors
                        
                  except:
                     list_task_errors.append(name + " >>> """ + str(task) + " >>> Unvollständige Angaben") 
                     return list_task_errors                   

               else:
                  if task_type == "controller":
                     list_task_errors.append(name + " >>> " + controller_command + " >>> Ungültiger Befehl >>> " + task[1])
                  else:
                     list_task_errors.append(name + " >>> """ + task[1] + " >>> Ungültiger Befehl")
                  return list_task_errors


            except:
               if task_type == "controller":
                  list_task_errors.append(name + " >>> " + controller_command + " >>> fehlende Einstellung >>> Befehl") 
               else:
                  list_task_errors.append(name + " >>> Befehl >>> fehlende Einstellung") 
               return list_task_errors

                               
         else:
            if task_type == "controller":
               list_task_errors.append(name + " >>> " + controller_command + " >>> Ungültige Formatierung")
            else:
               list_task_errors.append(name + " >>> Ungültige Formatierung")   
            return list_task_errors
            

      # ########################
      #  task "None" controller
      # ########################
      
      if "None" in task and task_type == "controller": 
         return list_task_errors


      # ###############
      #  nothing found
      # ###############
      
      
      if task_type == "controller":
         list_task_errors.append(name + " >>> " + controller_command + " >>> Ungültige Aufgabe") 
      else:
         list_task_errors.append(name + " >>> Ungültige Aufgabe")
         
      return list_task_errors
   
   
   except Exception as e:
      
      if task_type == "controller":
         list_task_errors.append(name + " >>> " + controller_command + " >>> Ungültige Aufgabe")   
      else:
         list_task_errors.append("MISSING NAME >>> Ungültige Aufgabe") 
         
      return list_task_errors
