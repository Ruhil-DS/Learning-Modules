"?5
BHostIDLE"IDLE1     v?@A     v?@a?????i??????Unknown
?HostSquaredDifference"$mean_squared_error/SquaredDifference(1     Ԕ@9     Ԕ@A     Ԕ@I     Ԕ@a?????7??iK??????Unknown
?HostDataset"4Iterator::Root::ParallelMapV2::Zip[1]::ForeverRepeat(1     0?@9     0?@A     ?@I     ?@a??0Њ???i2??n?:???Unknown
{HostMatMul"'gradient_tape/model_3/aux_output/MatMul(1     ??@9     ??@A     ??@I     ??@a,?tv?I??i??\=?????Unknown
uHostFlushSummaryWriter"FlushSummaryWriter(1     ?J@9     ?J@A     ?J@I     ?J@a??{?sx?i??R??????Unknown?
{HostMatMul"'gradient_tape/model_3/dense_23/MatMul_1(1     ?A@9     ?A@A     ?A@I     ?A@a(eJ??%p?id*G????Unknown
rHostConcatV2"model_3/concatenate_9/concat(1      ?@9      ?@A      ?@I      ?@a?6_?ɚl?i??L?1???Unknown
rHostDataset"Iterator::Root::ParallelMapV2(1      >@9      >@A      >@I      >@a?????k?im???dM???Unknown
y	HostMatMul"%gradient_tape/model_3/dense_23/MatMul(1      <@9      <@A      <@I      <@a?w?!?i?iu@?:g???Unknown
o
Host_FusedMatMul"model_3/dense_22/Relu(1      9@9      9@A      9@I      9@a?َeyg?iO??xL~???Unknown
?HostDataset">Iterator::Root::ParallelMapV2::Zip[0]::FlatMap[0]::Concatenate(1      @@9      @@A      7@I      7@a??H	9e?i_?????Unknown
cHostDataset"Iterator::Root(1      H@9      H@A      2@I      2@a?q??`?iw?r!????Unknown
oHost_FusedMatMul"model_3/dense_23/Relu(1      2@9      2@A      2@I      2@a?q??`?i?w?c?????Unknown
iHostWriteSummary"WriteSummary(1      0@9      0@A      0@I      0@a?????]?i?M???????Unknown?
yHostMatMul"%gradient_tape/model_3/dense_22/MatMul(1      0@9      0@A      0@I      0@a?????]?i+$?eD????Unknown
|HostMatMul"(gradient_tape/model_3/main_output/MatMul(1      0@9      0@A      0@I      0@a?????]?iy???????Unknown
`HostGatherV2"
GatherV2_2(1      ,@9      ,@A      ,@I      ,@a?w?!?Y?i?5h??????Unknown
?HostResourceApplyGradientDescent"-SGD/SGD/update_5/ResourceApplyGradientDescent(1      *@9      *@A      *@I      *@a?>?s??W?i$"??????Unknown
wHostDataset""Iterator::Root::ParallelMapV2::Zip(1     ??@9     ??@A      (@I      (@a?tAWA%V?i???p???Unknown
tHost_FusedMatMul"model_3/aux_output/BiasAdd(1      (@9      (@A      (@I      (@a?tAWA%V?i?ey???Unknown
?HostResourceApplyGradientDescent"-SGD/SGD/update_4/ResourceApplyGradientDescent(1      &@9      &@A      &@I      &@a??:?LT?i??z=???Unknown
tHostAssignAddVariableOp"AssignAddVariableOp(1      $@9      $@A      $@I      $@aR?atR?i׾??w#???Unknown
?HostDataset"@Iterator::Root::ParallelMapV2::Zip[1]::ForeverRepeat::FromTensor(1      $@9      @A      $@I      @aR?atR?i??4۱,???Unknown
lHostIteratorGetNext"IteratorGetNext(1      $@9      $@A      $@I      $@aR?atR?i????5???Unknown
?HostResourceApplyGradientDescent"-SGD/SGD/update_1/ResourceApplyGradientDescent(1      $@9      $@A      $@I      $@aR?atR?i??R<&????Unknown
?HostResourceApplyGradientDescent"-SGD/SGD/update_6/ResourceApplyGradientDescent(1      $@9      $@A      $@I      $@aR?atR?i???l`H???Unknown
?HostDynamicStitch".gradient_tape/mean_squared_error/DynamicStitch(1      $@9      $@A      $@I      $@aR?atR?i??p??Q???Unknown
~HostMatMul"*gradient_tape/model_3/main_output/MatMul_1(1      $@9      $@A      $@I      $@aR?atR?i}????Z???Unknown
^HostGatherV2"GatherV2(1      "@9      "@A      "@I      "@a?q??P?i	???"c???Unknown
?HostDataset"NIterator::Root::ParallelMapV2::Zip[0]::FlatMap[0]::Concatenate[0]::TensorSlice(1      "@9      "@A      "@I      "@a?q??P?i?S?pk???Unknown
?HostResourceApplyGradientDescent"-SGD/SGD/update_2/ResourceApplyGradientDescent(1      "@9      "@A      "@I      "@a?q??P?i!???s???Unknown
? HostResourceApplyGradientDescent"-SGD/SGD/update_3/ResourceApplyGradientDescent(1      "@9      "@A      "@I      "@a?q??P?i???|???Unknown
?!HostBiasAddGrad"2gradient_tape/model_3/dense_22/BiasAdd/BiasAddGrad(1      "@9      "@A      "@I      "@a?q??P?i9}??Z????Unknown
?"HostBiasAddGrad"5gradient_tape/model_3/main_output/BiasAdd/BiasAddGrad(1      "@9      "@A      "@I      "@a?q??P?i?5??????Unknown
u#HostSum"$mean_squared_error/weighted_loss/Sum(1      "@9      "@A      "@I      "@a?q??P?iQ?????Unknown
`$HostGatherV2"
GatherV2_1(1       @9       @A       @I       @a?????M?ixY?YX????Unknown
`%HostGatherV2"
GatherV2_3(1       @9       @A       @I       @a?????M?i??i?????Unknown
?&HostResourceApplyGradientDescent"+SGD/SGD/update/ResourceApplyGradientDescent(1       @9       @A       @I       @a?????M?i?/??????Unknown
?'HostResourceApplyGradientDescent"-SGD/SGD/update_7/ResourceApplyGradientDescent(1       @9       @A       @I       @a?????M?i??N?}????Unknown
?(HostBiasAddGrad"4gradient_tape/model_3/aux_output/BiasAdd/BiasAddGrad(1       @9       @A       @I       @a?????M?i?[߹???Unknown
u)Host_FusedMatMul"model_3/main_output/BiasAdd(1       @9       @A       @I       @a?????M?i;q3A????Unknown
g*HostStridedSlice"strided_slice(1       @9       @A       @I       @a?????M?ibܥܢ????Unknown
e+Host
LogicalAnd"
LogicalAnd(1      @9      @A      @I      @a?w?!?I?i$?	e????Unknown?
?,HostDynamicStitch"0gradient_tape/mean_squared_error_1/DynamicStitch(1      @9      @A      @I      @a?w?!?I?i?n??????Unknown
}-HostMatMul")gradient_tape/model_3/aux_output/MatMul_1(1      @9      @A      @I      @a?w?!?I?i?5?u????Unknown
?.HostBiasAddGrad"2gradient_tape/model_3/dense_23/BiasAdd/BiasAddGrad(1      @9      @A      @I      @a?w?!?I?ijS6?x????Unknown
?/HostTile"5gradient_tape/mean_squared_error/weighted_loss/Tile_1(1      @9      @A      @I      @a?tAWA%F?i?#?N????Unknown
X0HostCast"Cast_2(1      @9      @A      @I      @aR?atB?i???f?????Unknown
?1HostTile"7gradient_tape/mean_squared_error_1/weighted_loss/Tile_1(1      @9      @A      @I      @aR?atB?i?)<????Unknown
~2HostSlice"+gradient_tape/model_3/concatenate_9/Slice_1(1      @9      @A      @I      @aR?atB?i??b??????Unknown
?3HostSquaredDifference"&mean_squared_error_1/SquaredDifference(1      @9      @A      @I      @aR?atB?i?/??v????Unknown
?4HostDataset".Iterator::Root::ParallelMapV2::Zip[0]::FlatMap(1     ?A@9     ?A@A      @I      @a?tAWA%6?i??W;????Unknown
w5HostReadVariableOp"SGD/Identity/ReadVariableOp(1       @9       @A       @I       @a?????-?i????????Unknown
a6HostIdentity"Identity(1      ??9      ??A      ??I      ??a??????i     ???Unknown?*?4
?HostSquaredDifference"$mean_squared_error/SquaredDifference(1     Ԕ@9     Ԕ@A     Ԕ@I     Ԕ@ay?	????iy?	?????Unknown
?HostDataset"4Iterator::Root::ParallelMapV2::Zip[1]::ForeverRepeat(1     0?@9     0?@A     ?@I     ?@a?[
?I???i???/????Unknown
{HostMatMul"'gradient_tape/model_3/aux_output/MatMul(1     ??@9     ??@A     ??@I     ??@anNWy&>??i8??v?8???Unknown
uHostFlushSummaryWriter"FlushSummaryWriter(1     ?J@9     ?J@A     ?J@I     ?J@am#??$??iN|?wK????Unknown?
{HostMatMul"'gradient_tape/model_3/dense_23/MatMul_1(1     ?A@9     ?A@A     ?A@I     ?A@a???{?C??i???Y????Unknown
rHostConcatV2"model_3/concatenate_9/concat(1      ?@9      ?@A      ?@I      ?@a?1͠??~?ieQ??#???Unknown
rHostDataset"Iterator::Root::ParallelMapV2(1      >@9      >@A      >@I      >@a?'?j?}?i??#??^???Unknown
yHostMatMul"%gradient_tape/model_3/dense_23/MatMul(1      <@9      <@A      <@I      <@a9?_R?{?i???,?????Unknown
o	Host_FusedMatMul"model_3/dense_22/Relu(1      9@9      9@A      9@I      9@a?????x?i? ?F????Unknown
?
HostDataset">Iterator::Root::ParallelMapV2::Zip[0]::FlatMap[0]::Concatenate(1      @@9      @@A      7@I      7@a??,???v?i?i??????Unknown
cHostDataset"Iterator::Root(1      H@9      H@A      2@I      2@a??????q?i??h+???Unknown
oHost_FusedMatMul"model_3/dense_23/Relu(1      2@9      2@A      2@I      2@a??????q?iV!?;???Unknown
iHostWriteSummary"WriteSummary(1      0@9      0@A      0@I      0@a?;????o?i??ם@[???Unknown?
yHostMatMul"%gradient_tape/model_3/dense_22/MatMul(1      0@9      0@A      0@I      0@a?;????o?i?? ?z???Unknown
|HostMatMul"(gradient_tape/model_3/main_output/MatMul(1      0@9      0@A      0@I      0@a?;????o?i
?D?c????Unknown
`HostGatherV2"
GatherV2_2(1      ,@9      ,@A      ,@I      ,@a9?_R?k?iA??????Unknown
?HostResourceApplyGradientDescent"-SGD/SGD/update_5/ResourceApplyGradientDescent(1      *@9      *@A      *@I      *@a~ I4:?i?i??/?????Unknown
wHostDataset""Iterator::Root::ParallelMapV2::Zip(1     ??@9     ??@A      (@I      (@a???"?g?ik?QV????Unknown
tHost_FusedMatMul"model_3/aux_output/BiasAdd(1      (@9      (@A      (@I      (@a???"?g?i?K?s????Unknown
?HostResourceApplyGradientDescent"-SGD/SGD/update_4/ResourceApplyGradientDescent(1      &@9      &@A      &@I      &@a?x?	?e?i???}????Unknown
tHostAssignAddVariableOp"AssignAddVariableOp(1      $@9      $@A      $@I      $@aM????c?i??yor(???Unknown
?HostDataset"@Iterator::Root::ParallelMapV2::Zip[1]::ForeverRepeat::FromTensor(1      $@9      @A      $@I      @aM????c?i[?+a-<???Unknown
lHostIteratorGetNext"IteratorGetNext(1      $@9      $@A      $@I      $@aM????c?i ??R?O???Unknown
?HostResourceApplyGradientDescent"-SGD/SGD/update_1/ResourceApplyGradientDescent(1      $@9      $@A      $@I      $@aM????c?i??D?c???Unknown
?HostResourceApplyGradientDescent"-SGD/SGD/update_6/ResourceApplyGradientDescent(1      $@9      $@A      $@I      $@aM????c?i?B6^w???Unknown
?HostDynamicStitch".gradient_tape/mean_squared_error/DynamicStitch(1      $@9      $@A      $@I      $@aM????c?io)?'????Unknown
~HostMatMul"*gradient_tape/model_3/main_output/MatMul_1(1      $@9      $@A      $@I      $@aM????c?i4:?Ԟ???Unknown
^HostGatherV2"GatherV2(1      "@9      "@A      "@I      "@a??????a?i??,??????Unknown
?HostDataset"NIterator::Root::ParallelMapV2::Zip[0]::FlatMap[0]::Concatenate[0]::TensorSlice(1      "@9      "@A      "@I      "@a??????a?i????W????Unknown
?HostResourceApplyGradientDescent"-SGD/SGD/update_2/ResourceApplyGradientDescent(1      "@9      "@A      "@I      "@a??????a?iJ4:?????Unknown
?HostResourceApplyGradientDescent"-SGD/SGD/update_3/ResourceApplyGradientDescent(1      "@9      "@A      "@I      "@a??????a?i????????Unknown
? HostBiasAddGrad"2gradient_tape/model_3/dense_22/BiasAdd/BiasAddGrad(1      "@9      "@A      "@I      "@a??????a?i??GY?????Unknown
?!HostBiasAddGrad"5gradient_tape/model_3/main_output/BiasAdd/BiasAddGrad(1      "@9      "@A      "@I      "@a??????a?i`.?2_	???Unknown
u"HostSum"$mean_squared_error/weighted_loss/Sum(1      "@9      "@A      "@I      "@a??????a?i?T!???Unknown
`#HostGatherV2"
GatherV2_1(1       @9       @A       @I       @a?;????_?i????*???Unknown
`$HostGatherV2"
GatherV2_3(1       @9       @A       @I       @a?;????_?iNX??:???Unknown
?%HostResourceApplyGradientDescent"+SGD/SGD/update/ResourceApplyGradientDescent(1       @9       @A       @I       @a?;????_?i??fP{J???Unknown
?&HostResourceApplyGradientDescent"-SGD/SGD/update_7/ResourceApplyGradientDescent(1       @9       @A       @I       @a?;????_?i???DZ???Unknown
?'HostBiasAddGrad"4gradient_tape/model_3/aux_output/BiasAdd/BiasAddGrad(1       @9       @A       @I       @a?;????_?i(?j???Unknown
u(Host_FusedMatMul"model_3/main_output/BiasAdd(1       @9       @A       @I       @a?;????_?i?Zx??y???Unknown
g)HostStridedSlice"strided_slice(1       @9       @A       @I       @a?;????_?id??U?????Unknown
e*Host
LogicalAnd"
LogicalAnd(1      @9      @A      @I      @a9?_R?[?i?s?m????Unknown?
?+HostDynamicStitch"0gradient_tape/mean_squared_error_1/DynamicStitch(1      @9      @A      @I      @a9?_R?[?ixL3?=????Unknown
},HostMatMul")gradient_tape/model_3/aux_output/MatMul_1(1      @9      @A      @I      @a9?_R?[?i%cQ????Unknown
?-HostBiasAddGrad"2gradient_tape/model_3/dense_23/BiasAdd/BiasAddGrad(1      @9      @A      @I      @a9?_R?[?i?????????Unknown
?.HostTile"5gradient_tape/mean_squared_error/weighted_loss/Tile_1(1      @9      @A      @I      @a???"?W?in???????Unknown
X/HostCast"Cast_2(1      @9      @A      @I      @aM????S?ievp?????Unknown
?0HostTile"7gradient_tape/mean_squared_error_1/weighted_loss/Tile_1(1      @9      @A      @I      @aM????S?i?~I}n????Unknown
~1HostSlice"+gradient_tape/model_3/concatenate_9/Slice_1(1      @9      @A      @I      @aM????S?i+?"?K????Unknown
?2HostSquaredDifference"&mean_squared_error_1/SquaredDifference(1      @9      @A      @I      @aM????S?i???n)????Unknown
?3HostDataset".Iterator::Root::ParallelMapV2::Zip[0]::FlatMap(1     ?A@9     ?A@A      @I      @a???"?G?i??}?????Unknown
w4HostReadVariableOp"SGD/Identity/ReadVariableOp(1       @9       @A       @I       @a?;??????i????????Unknown
a5HostIdentity"Identity(1      ??9      ??A      ??I      ??a?;????/?i     ???Unknown?2CPU