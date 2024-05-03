<?php
/**
 * Class: OpenEI.php - Clean, simple API to basic OpenEI functionality
 * @author jay huggins, jon weers
 * @uses localSettings.php
 * Example Usage:
 *    $results = OpenEI::ask($query);
 *  -or-
 *    $results = OpenEI::ask('[[Category::Utility Companies]]|?Name|?Location');
 */

require_once 'assets/localSettings.php';

class OpenEI {

  const debug = false;

  /**
   * ask (query)
   * Performs an Ask Query against the OpenEI wiki.
   * Query should be formatted in wiki syntax, for example:
   *   $query = "[[Category:Things]] [[Property::Foo]] [[Bar::+]] |?Bar"
   * @param string $query
   * @param int limit (optional, default 1000)
   * @param int offset (optional, deafult 0)
   * @return array $result_objects
   */
  static function ask($query,$limit=1000,$offset=0){
    $limit = is_int($limit)? $limit : 1000;
    $offset = is_int($offset)? $offset : 0;
    $params = array(
      'limit' => $limit,
      'offset' => $offset,
      'format' => 'json'
    );
    //Assemble Request
    $requestUri = Settings::askUrl . str_replace(array('-',' ','[',']','?','/','|'),array('-2D','-20','-5B','-5D','-3F','-2F','/'),$query);
    foreach ($params as $param => $val){
      $requestUri .= "/$param%3D$val";
    }
    if (self::debug){
      print "Request Uri: $requestUri\n";
    }
    //Fetch Response
    $rJson = '';
    $results = array();
    //Make sure it's fresh
    $ctx = array(
      'http'=>array(
        'method'=>"GET",
        'header'=>"Cache-Control: no-cache\r\n".
                  "Pragma: no-cache\r\n"
    ));
    if (Settings::useProxy){
        $ctx['http']['proxy'] = Settings::proxyUrl;
        $ctx['http']['request_fulluri'] = true;
        $ctx['ssl'] = array(
            'SNI_enabled' => true,
            'SNI_server_name' => parse_url(Settings::askUrl, PHP_URL_HOST)
            );
    }
    $context = stream_context_create($ctx);
    try {
        $rJson = file_get_contents($requestUri,false,$context);
        if ($rJson){
            $rObj = json_decode($rJson);
            $results = $rObj->results;
        }
    } catch (Exception $e){
        if (self::debug){
            print "Error fetching response:\n$e\n";
        }
    }
    return $results;
  }
  //End class
}

?>
